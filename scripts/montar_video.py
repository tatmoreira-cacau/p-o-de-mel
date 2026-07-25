#!/usr/bin/env python3
"""Monta um vídeo vertical narrado a partir de fotos + um áudio de narração.

As fotos entram na ordem do nome do arquivo (01, 02, 03...), cada uma com um zoom
lento, e os cortes caem nas pausas naturais da fala — não em intervalos fixos.
É isso que faz o slideshow parecer editado à mão em vez de automático.

Uso:
    python3 scripts/montar_video.py --fotos fotos/ --audio narracao.m4a --saida video.mp4

Opções úteis:
    --apertar-pausas 0.35   corta pausas longas (ganha tempo sem perder palavra)
    --textos textos.json    sobrepõe texto na tela em trechos definidos
    --max-duracao 180       corta o fim do áudio nesse limite (ex.: 3 min do Reels)
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

W, H = 1080, 1920
FPS = 30
FADE = 0.5  # duração do crossfade entre fotos
SUP = 1.5   # super-amostragem antes do zoompan, senão a imagem treme


def ffmpeg_bin() -> str:
    for cand in ("ffmpeg", "ffprobe"):
        if shutil.which(cand) and cand == "ffmpeg":
            return "ffmpeg"
    try:
        import imageio_ffmpeg

        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit("ffmpeg não encontrado. Instale com: pip install imageio-ffmpeg")


FF = ffmpeg_bin()


def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def duracao(caminho: Path) -> float:
    out = run([FF, "-i", str(caminho)]).stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out)
    if not m:
        sys.exit(f"não consegui ler a duração de {caminho}")
    h, mi, s = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(s)


def preparar_audio(entrada: Path, saida: Path, apertar: float | None, limite: float | None) -> float:
    """Normaliza o volume e, opcionalmente, encurta as pausas longas."""
    filtros = []
    if apertar:
        # Reduz toda pausa maior que `apertar` para exatamente `apertar` segundos.
        filtros.append(
            f"silenceremove=stop_periods=-1:stop_duration={apertar}"
            f":stop_threshold=-30dB:detection=peak"
        )
    filtros.append("loudnorm=I=-16:TP=-1.5:LRA=11")

    cmd = [FF, "-y", "-i", str(entrada), "-af", ",".join(filtros)]
    if limite:
        cmd += ["-t", str(limite)]
    cmd += ["-ar", "44100", "-ac", "2", "-c:a", "aac", "-b:a", "192k", str(saida)]
    r = run(cmd)
    if r.returncode != 0:
        sys.exit(f"falha ao preparar o áudio:\n{r.stderr[-2000:]}")
    return duracao(saida)


def pausas(audio: Path, limiar: str = "-20dB", minimo: float = 0.5) -> list[tuple[float, float]]:
    """Devolve os intervalos de silêncio (início, fim) detectados na narração."""
    r = run([FF, "-i", str(audio), "-af", f"silencedetect=n={limiar}:d={minimo}", "-f", "null", "-"])
    inicios = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", r.stderr)]
    fins = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", r.stderr)]
    return list(zip(inicios, fins))


def cortes(total: float, n: int, silencios: list[tuple[float, float]]) -> list[float]:
    """Escolhe n-1 pontos de corte: os alvos são igualmente espaçados, mas cada um
    escorrega para a pausa mais próxima. Assim a foto troca quando ela respira."""
    if n < 2:
        return []
    candidatos = [(a + b) / 2 for a, b in silencios]
    pontos = []
    anterior = 0.0
    for i in range(1, n):
        alvo = total * i / n
        # só serve pausa que deixe pelo menos 1.2s para a foto anterior
        viaveis = [c for c in candidatos if c > anterior + 1.2 and c < total - 1.2]
        escolhido = min(viaveis, key=lambda c: abs(c - alvo)) if viaveis else alvo
        # se a pausa mais próxima estiver longe demais, o ritmo fica estranho:
        # nesse caso vale mais respeitar o espaçamento regular
        if abs(escolhido - alvo) > total / n * 0.45:
            escolhido = alvo
        pontos.append(escolhido)
        anterior = escolhido
    return pontos


def clipe(imagem: Path, dur: float, destino: Path, indice: int) -> None:
    """Renderiza uma foto como clipe com zoom lento (Ken Burns)."""
    frames = max(2, int(round(dur * FPS)))
    sw, sh = int(W * SUP), int(H * SUP)
    # alterna aproximar / afastar para o vídeo não ficar monótono
    if indice % 2 == 0:
        z = f"min(zoom+{0.12 / frames:.8f},1.12)"
    else:
        z = f"if(lte(zoom,1.0),1.12,max(zoom-{0.12 / frames:.8f},1.0))"
    vf = (
        f"scale={sw}:{sh}:force_original_aspect_ratio=increase,crop={sw}:{sh},"
        f"zoompan=z='{z}':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
        f":s={W}x{H}:fps={FPS},setsar=1"
    )
    # A entrada precisa ser um único quadro: o zoompan gera `d` quadros para CADA
    # quadro que recebe, então alimentá-lo com "-loop 1" multiplica a duração
    # (3s viram 256s) e a renderização nunca acaba.
    r = run([
        FF, "-y", "-i", str(imagem),
        "-vf", vf, "-frames:v", str(frames),
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "16",
        "-pix_fmt", "yuv420p", "-an", str(destino),
    ])
    if r.returncode != 0:
        sys.exit(f"falha ao renderizar {imagem.name}:\n{r.stderr[-2000:]}")


def png_texto(texto: str, destino: Path) -> None:
    """Desenha o texto de tela num PNG transparente, para sobrepor ao vídeo."""
    from PIL import Image, ImageDraw, ImageFont

    fontes = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    caminho = next((f for f in fontes if Path(f).exists()), None)
    if not caminho:
        sys.exit("nenhuma fonte encontrada para desenhar o texto")

    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    tamanho = 64
    fonte = ImageFont.truetype(caminho, tamanho)
    # encolhe até caber com margem, senão o texto sangra na borda do celular
    while tamanho > 30:
        largura = max(d.textlength(l, font=fonte) for l in texto.split("\n"))
        if largura <= W * 0.84:
            break
        tamanho -= 4
        fonte = ImageFont.truetype(caminho, tamanho)

    d.multiline_text(
        (W / 2, H * 0.74), texto, font=fonte, fill=(255, 255, 255, 255),
        anchor="mm", align="center", spacing=18,
        stroke_width=5, stroke_fill=(0, 0, 0, 170),
    )
    img.save(destino)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--fotos", required=True, type=Path, help="pasta com as imagens numeradas")
    p.add_argument("--audio", required=True, type=Path, help="áudio da narração")
    p.add_argument("--saida", default=Path("video.mp4"), type=Path)
    p.add_argument("--apertar-pausas", type=float, default=None, metavar="SEG")
    p.add_argument("--max-duracao", type=float, default=None, metavar="SEG")
    p.add_argument("--textos", type=Path, default=None,
                   help='JSON: [{"texto": "...", "inicio": 0, "fim": 6}]')
    p.add_argument("--trilha", type=Path, default=None, help="música de fundo (opcional)")
    p.add_argument("--volume-trilha", type=float, default=0.15)
    args = p.parse_args()

    exts = {".jpg", ".jpeg", ".png", ".webp", ".heic"}
    imagens = sorted(f for f in args.fotos.iterdir() if f.suffix.lower() in exts)
    if not imagens:
        sys.exit(f"nenhuma imagem encontrada em {args.fotos}")

    tmp = Path(tempfile.mkdtemp(prefix="montagem-"))
    print(f"{len(imagens)} fotos · trabalhando em {tmp}")

    audio = tmp / "narracao.m4a"
    total = preparar_audio(args.audio, audio, args.apertar_pausas, args.max_duracao)
    print(f"áudio pronto: {total:.1f}s ({total/60:.1f} min)")

    sil = pausas(audio)
    pontos = cortes(total, len(imagens), sil)
    limites = [0.0] + pontos + [total]
    duracoes = [limites[i + 1] - limites[i] for i in range(len(imagens))]
    print(f"{len(sil)} pausas detectadas · cortes em: " +
          ", ".join(f"{t:.0f}s" for t in pontos[:12]) + ("..." if len(pontos) > 12 else ""))

    clipes = []
    for i, (img, dur) in enumerate(zip(imagens, duracoes)):
        # cada clipe carrega o crossfade seguinte, por isso ganha FADE a mais
        extra = FADE if i < len(imagens) - 1 else 0.0
        destino = tmp / f"clipe_{i:03d}.mp4"
        clipe(img, dur + extra, destino, i)
        clipes.append((destino, dur))
        print(f"  [{i+1:2d}/{len(imagens)}] {img.name} → {dur:.1f}s")

    # encadeia os clipes com crossfade
    entradas, filtro, atual, deslocamento = [], [], "0:v", 0.0
    for i, (caminho, _) in enumerate(clipes):
        entradas += ["-i", str(caminho)]
    for i in range(1, len(clipes)):
        deslocamento += clipes[i - 1][1] - (FADE if i > 1 else 0)
        rotulo = f"x{i}"
        filtro.append(
            f"[{atual}][{i}:v]xfade=transition=fade:duration={FADE}"
            f":offset={deslocamento:.3f}[{rotulo}]"
        )
        atual = rotulo
    saida_v = f"[{atual}]" if len(clipes) > 1 else "[0:v]"

    # sobrepõe os textos de tela
    if args.textos:
        overlays = json.loads(args.textos.read_text(encoding="utf-8"))
        base = len(clipes)
        for j, ov in enumerate(overlays):
            png = tmp / f"txt_{j:03d}.png"
            png_texto(ov["texto"], png)
            # o -t é obrigatório: sem ele a imagem em loop é uma entrada infinita
            # e a montagem nunca termina
            entradas += ["-loop", "1", "-t", f"{total:.3f}", "-i", str(png)]
            rotulo = f"o{j}"
            filtro.append(
                f"{saida_v}[{base + j}:v]overlay=0:0"
                f":enable='between(t,{ov['inicio']},{ov['fim']})'[{rotulo}]"
            )
            saida_v = f"[{rotulo}]"

    idx_audio = len(clipes) + (len(json.loads(args.textos.read_text(encoding='utf-8'))) if args.textos else 0)
    entradas += ["-i", str(audio)]
    mapa_audio = f"{idx_audio}:a"

    if args.trilha:
        entradas += ["-i", str(args.trilha)]
        filtro.append(
            f"[{idx_audio + 1}:a]volume={args.volume_trilha},aloop=loop=-1:size=2e9[bg];"
            f"[{idx_audio}:a][bg]amix=inputs=2:duration=first:dropout_transition=0[aout]"
        )
        mapa_audio = "[aout]"

    cmd = [FF, "-y", *entradas]
    if filtro:
        cmd += ["-filter_complex", ";".join(filtro)]
    cmd += [
        "-map", saida_v if filtro else "0:v",
        "-map", mapa_audio,
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
        "-shortest", str(args.saida),
    ]
    print("montando...")
    r = run(cmd)
    if r.returncode != 0:
        sys.exit(f"falha na montagem:\n{r.stderr[-3000:]}")

    print(f"\npronto: {args.saida}  ({duracao(args.saida):.1f}s · {W}x{H})")


if __name__ == "__main__":
    main()

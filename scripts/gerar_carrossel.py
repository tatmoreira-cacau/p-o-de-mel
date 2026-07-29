#!/usr/bin/env python3
"""Gera as imagens de um carrossel de Instagram a partir de um JSON de slides.

Formato 4:5 (1080x1350), que é o que ocupa mais altura no feed e por isso
segura mais tempo o polegar de quem rola.

Uso:
    python3 scripts/gerar_carrossel.py --slides carrossel/historia.json --saida carrossel/
"""

import argparse
import json
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
MARGEM = 110

# A paleta sai do próprio produto: chocolate e o rosa do bolo.
CORES = {
    "chocolate": {"fundo": (58, 35, 24), "texto": (245, 237, 228), "detalhe": (232, 169, 184)},
    "creme": {"fundo": (245, 237, 228), "texto": (58, 35, 24), "detalhe": (200, 122, 143)},
    "rosa": {"fundo": (247, 220, 227), "texto": (58, 35, 24), "detalhe": (150, 80, 100)},
}

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def ajustar(texto: str, fonte_path: str, largura_max: int, altura_max: int,
            tam_inicial: int = 78, tam_min: int = 34):
    """Escolhe o maior corpo de fonte em que o texto ainda cabe na área útil.

    Sem isso, uma frase mais longa que as outras estoura a margem e o slide sai
    com texto encostado na borda — que é onde o Instagram corta na pré-visualização.
    """
    tam = tam_inicial
    while tam >= tam_min:
        fonte = ImageFont.truetype(fonte_path, tam)
        # ~1.9 caracteres por unidade de fonte é uma estimativa boa para serifada
        cols = max(12, int(largura_max / (tam * 0.52)))
        linhas = textwrap.wrap(texto, width=cols)
        alt_linha = tam * 1.34
        if len(linhas) * alt_linha <= altura_max:
            larguras = [fonte.getlength(l) for l in linhas]
            if max(larguras) <= largura_max:
                return fonte, linhas, alt_linha
        tam -= 3
    fonte = ImageFont.truetype(fonte_path, tam_min)
    return fonte, textwrap.wrap(texto, width=30), tam_min * 1.34


def desenhar(slide: dict, numero: int, total: int, destino: Path, arroba: str) -> None:
    tema = CORES[slide.get("estilo", "creme")]
    img = Image.new("RGB", (W, H), tema["fundo"])
    d = ImageDraw.Draw(img)

    util_l = W - MARGEM * 2
    topo, base = MARGEM, H - MARGEM - 60  # o rodapé fica abaixo de `base`
    util_a = base - topo

    negrito = slide.get("peso", "bold") == "bold"
    fonte, linhas, alt_linha = ajustar(
        slide["texto"], SERIF_BOLD if negrito else SERIF, util_l, util_a - 160,
        tam_inicial=slide.get("tamanho", 78),
    )

    f_etiqueta = ImageFont.truetype(SANS, 30)
    f_apoio = ImageFont.truetype(SANS, 36)
    linhas_apoio = textwrap.wrap(slide["apoio"], width=42) if slide.get("apoio") else []

    # Mede o conteúdo inteiro antes de desenhar, para centralizar o bloco como um
    # todo. Centralizar só a frase deixa o slide visivelmente torto quando existe
    # etiqueta em cima ou linha de apoio embaixo.
    altura = len(linhas) * alt_linha
    if slide.get("etiqueta"):
        altura += 62
    if linhas_apoio:
        altura += 26 + len(linhas_apoio) * 50

    y = topo + max(0, (util_a - altura) / 2)

    if slide.get("etiqueta"):
        d.text((MARGEM, y), slide["etiqueta"].upper(), font=f_etiqueta, fill=tema["detalhe"])
        y += 62

    for linha in linhas:
        d.text((MARGEM, y), linha, font=fonte, fill=tema["texto"])
        y += alt_linha

    if linhas_apoio:
        y += 26
        for linha in linhas_apoio:
            d.text((MARGEM, y), linha, font=f_apoio, fill=tema["detalhe"])
            y += 50

    # rodapé: arroba à esquerda, contador à direita
    f_pe = ImageFont.truetype(SANS, 28)
    y_pe = H - MARGEM + 10
    d.text((MARGEM, y_pe), arroba, font=f_pe, fill=tema["detalhe"])
    contador = f"{numero}/{total}"
    d.text((W - MARGEM - f_pe.getlength(contador), y_pe), contador,
           font=f_pe, fill=tema["detalhe"])

    # filete de cor no topo, que costura os slides como uma série só
    d.rectangle([0, 0, W, 10], fill=tema["detalhe"])

    img.save(destino, quality=95)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--slides", required=True, type=Path)
    p.add_argument("--saida", required=True, type=Path)
    p.add_argument("--arroba", default="@cacaupitanga_")
    args = p.parse_args()

    dados = json.loads(args.slides.read_text(encoding="utf-8"))
    args.saida.mkdir(parents=True, exist_ok=True)
    total = len(dados)
    for i, slide in enumerate(dados, 1):
        destino = args.saida / f"slide_{i:02d}.png"
        desenhar(slide, i, total, destino, args.arroba)
        print(f"  {destino.name}  {slide['texto'][:52]}...")
    print(f"\n{total} slides em {args.saida}")


if __name__ == "__main__":
    main()

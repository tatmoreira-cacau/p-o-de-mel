# Especificações de Design — números exatos

Leia este arquivo antes de gerar o arquivo final. Estes valores existem para
resolver diretamente as reclamações mais comuns (fonte pequena, cor
desproporcional, conteúdo achatado).

## LEITURA EM CELULAR É PRIORIDADE (mobile-first)

O material é lido no **telefone**. Isso é a regra que manda em todas as outras:

- **Coluna única, sempre.** Nada de 2 colunas — no celular vira ilegível.
- **Formato de página vertical e estreito**, no proporção de tela de celular
  (ex.: página de ~9×16 cm em vez de A4). Assim o PDF enche a tela sem o leitor
  precisar dar zoom.
- **Fontes ainda maiores** que num PDF de computador: corpo em 15–17pt.
- **Margens menores** (1–1.5cm) para não desperdiçar a tela pequena, mas mantendo
  respiro entre blocos.
- **Nada que exija zoom ou rolagem lateral.** Se o leitor precisa apertar os
  olhos ou arrastar para o lado, o design falhou.
- Prefira **entregar também um HTML responsivo** (reflui no tamanho da tela) —
  é o formato mais confortável no celular. O PDF estreito é o plano B.

## Tipografia (resolve "letras/fontes pequenas")

| Elemento            | Tamanho        | Entrelinha | Peso        |
|---------------------|----------------|------------|-------------|
| Corpo de texto      | 12–14pt        | 1.5–1.6    | Regular     |
| H1 (capítulo)       | 26–32pt        | 1.2        | Bold        |
| H2 (seção)          | 20–24pt        | 1.25       | Bold/Semi   |
| H3 (subseção)       | 16–18pt        | 1.3        | Semibold    |
| Legenda de imagem   | 10–11pt        | 1.4        | Itálico     |
| Destaque/callout    | 13–15pt        | 1.5        | Semibold    |

Regras:
- **Nunca** use corpo abaixo de 12pt. Ebook lido no celular precisa de fonte
  grande e entrelinha folgada.
- Use no máximo 2 famílias tipográficas: uma para títulos, uma para o corpo.
- Fontes seguras e legíveis: corpo em serifada humanista ou sans legível
  (ex.: Georgia, "Noto Serif", "Source Serif", Inter, "Open Sans"); títulos
  podem ter mais personalidade.
- Largura de linha confortável: 60–75 caracteres. Linha muito longa cansa.

## Espaçamento (resolve "conteúdo achatado/espremido")

- Espaço entre parágrafos: pelo menos 0.8em (não use só recuo).
- Espaço antes de um título: ~1.5–2em. Depois do título: ~0.6em.
- Margens da página: 2–2.5cm de cada lado. Respiro nas bordas é sinal de
  qualidade.
- Não encoste texto nas imagens — deixe ~1em de folga.

## Cores (resolve "cores desproporcionais")

Princípio: **paleta enxuta**. 1 cor principal + 1 de apoio + neutros. Cor demais
deixa o material amador e cansativo.

Estrutura recomendada:
- **1 cor principal** (marca) — títulos, destaques, detalhes.
- **1 cor de apoio** — usada com moderação em callouts ou linhas.
- **Neutros**: quase-preto para texto (ex.: #222), cinza para legendas,
  branco/quase-branco para o fundo.

Regras de contraste:
- Texto sobre fundo deve ter contraste alto (mire WCAG AA: 4.5:1 para corpo).
- Nunca texto claro sobre fundo claro, nem cores vibrantes em blocos grandes de
  texto — cansa a vista.
- Cor é tempero, não prato principal. A maior parte da página é texto escuro
  sobre fundo claro.

Se o material já tem identidade de marca (cores da confeitaria/infoproduto),
respeite-as, mas discipline o uso: escolha 2–3 tons e mantenha consistência.

## Imagens (resolve "imagens cortadas")

- `max-width: 100%`; altura automática para manter proporção.
- Centralize e dê margem vertical (~1.2em).
- Uma imagem por bloco visual; evite colar várias imagens espremidas.
- Se a resolução for baixa ou a imagem chegar cortada, sinalize ao usuário.

## Ritmo da página (resolve "texto demais")

- Alterne: título → parágrafo curto → lista → imagem → destaque.
- A cada ~2 parágrafos, ofereça um respiro (lista, destaque, imagem ou subtítulo).
- Use caixas de destaque (callout) para dicas, avisos e "pontos de ouro".
- Comece capítulos em página nova quando fizer sentido.

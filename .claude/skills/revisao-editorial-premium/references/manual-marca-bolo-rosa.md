# Manual de Marca — E-book B.A.BA do Bolo Rosa (Cacau Pitanga)

Fonte da verdade para a identidade visual. A versão original e completa está em
`assets/especificacoes-oficiais-bolo-rosa.html` (spec técnica aprovada). Este
resumo é o que a skill precisa ter à mão ao diagramar.

> **Regra central (do próprio manual):** *"O conteúdo textual é intocável. Estas
> especificações regem apenas a apresentação visual — qualquer novo elemento deve
> usar exclusivamente as cores, fontes e traços definidos aqui."*

## Direção visual
Limpo, profissional, feminino e acolhedor. Papel creme, serifada elegante para
títulos, sans leve para o corpo, filetes finos, **losangos dourados** como
divisores e imagens emolduradas com respiro.

## Paleta oficial + as duas cores novas

| Nome           | Hex       | Uso                                                        |
|----------------|-----------|------------------------------------------------------------|
| Vinho Cacau    | `#8C3A3B` | Títulos, numerais, caixas "Importante", divisórias         |
| Ocre Dourado   | `#D4A24E` | Nº de página, marcadores, losangos, caixas "Dica"          |
| Verde Sálvia   | `#6A7F7B` | Legendas, microtexto, filetes, caixas informativas         |
| Terracota      | `#B86B4B` | Avisos "O erro", contrapontos em comparativos              |
| Verde Cacau    | `#5A6B5D` | Corpo de texto sobre creme, bordas de tabela               |
| Creme Papel    | `#F8F5F0` | Fundo de todas as páginas                                  |
| **Rosé Bolo**  | `#C86B85` | **NOVA** — acentos femininos, títulos de destaque, selos   |
| **Azul Sereno**| `#4F6D8C` | **NOVA** — caixas "Passo/Info", links, detalhes de apoio   |

As duas cores novas (rosa e azul) foram escolhidas para conversar com a paleta:
o rosé puxa o "Bolo Rosa" a partir do vinho; o azul sereno equilibra o conjunto
sem competir com o dourado. Use-as como **acento**, não como cor dominante — a
maioria da página continua texto escuro sobre creme.

Contraste (AA): corpo #5A6B5D sobre creme ≈ 4,9:1 · títulos #8C3A3B ≈ 6,7:1.
Ao usar rosé/azul em texto, garanta o mesmo nível de contraste sobre o creme.

## Tipografia

- **Títulos:** *Playfair Display* (serifada elegante), peso 500–600.
- **Corpo:** *Montserrat* (sans leve), peso 400.
- **Legendas/citações:** *Playfair Display itálico*.

Tamanhos oficiais (leitura em computador/tablet — ver adaptação mobile abaixo):
H2 capítulo 20–31pt · H3 seção 13,5–16pt · kicker 6,8–7,7pt caixa-alta ·
corpo 9,4–10,6pt (line-height 1,48–1,72) · legendas 8,9–9,4pt itálico.

## ADAPTAÇÃO MOBILE (pedido da cliente: celular + fontes maiores)

O manual original mira A4 em computador/tablet. Para **leitura no celular** com
**fontes maiores**, adapte mantendo a identidade (cores, fontes, componentes):

- Corpo sobe para **16–18pt**; H2 ~26–28pt; H3 ~18–20pt.
- Página estreita no formato de celular (coluna única sempre; nunca 2 colunas).
- Margens menores (1–1,5cm), mas mantendo o respiro entre blocos.
- Prefira entregar **HTML responsivo** (reflui na tela) + PDF estreito como apoio.

Nada de zoom nem rolagem lateral. Se algo do manual conflitar com a leitura no
celular, a legibilidade no celular vence — sem trair a paleta e as fontes.

## Componentes visuais (usar bastante)

- **Abertura de capítulo:** numeral dourado + kicker (caixa-alta, sálvia) + H2
  centralizado + divisor losango.
- **Caixas de destaque** (padding 11–12px × 14–16px, rótulo caixa-alta + ícone):
  - **Dica** — fundo ocre 10%, borda ocre `#D4A24E` (truques da Tati).
  - **Importante** — fundo vinho 6%, borda vinho `#8C3A3B` (regras de ouro).
  - **Informação** — fundo sálvia 10%, borda sálvia `#6A7F7B` ("para que serve").
  - **Passo/Nota** — pode usar o **azul sereno** `#4F6D8C` como nova variação.
  - Nunca duas caixas do mesmo tipo em sequência na mesma página.
- **Passo a passo:** numerais Playfair em círculo (#8C3A3B) + foto-guia.
- **Divisor de seção:** filete 1px sálvia 50% + losango 5–6px (vinho no creme).
- **Rodapé:** número da página em Playfair #D4A24E entre dois filetes, centrado.
- **Cabeçalho corrente:** capítulo à esquerda (Montserrat caixa-alta, sálvia),
  wordmark "Cacau Pitanga" à direita (Playfair itálico dourado).
- **Imagens:** moldura sálvia 1px + legenda Playfair itálico centrada; respiro em
  volta; nunca cortadas ou distorcidas.
- **Ícones:** traço (outline) 1,4–1,8px, cantos arredondados, cores da paleta.

O CSS `assets/estilo-premium.css` já implementa esses componentes com a paleta
oficial + rosé + azul, já adaptado para fontes grandes e leitura no celular.

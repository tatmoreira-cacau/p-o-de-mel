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

## Paleta APROVADA (retirada da capa e do selo do e-book)

| Nome         | Hex       | Uso                                                          |
|--------------|-----------|--------------------------------------------------------------|
| Vinho        | `#8B2F4C` | Cor de capítulo, títulos, destaques, caixas "Importante"     |
| Verde        | `#5E7D68` | Cor de capítulo, divisórias de módulo, legendas, caixa "Nota"|
| Verde-menta  | `#A9C4B3` | Molduras de foto, bordas de cartão, fundos suaves (do selo)  |
| Dourado      | `#C6A05A` | Nº de página, marcadores, losangos, caixas "Dica"            |
| Creme Papel  | `#F6F1E7` | Fundo de todas as páginas                                    |
| Mesa (verde) | `#4E6A59` | Fundo ao redor da "tela" (moldura escura)                    |
| Tinta        | `#37413b` | Corpo de texto sobre creme                                   |

Regra: **verde e vinho são as duas cores principais** (do selo/flor da capa);
dourado, creme e menta são apoio. A maioria da página é texto escuro sobre creme
— cor é tempero, não prato principal.

### Cor por capítulo (pedido da cliente)
Cada capítulo/módulo tem sua **cor de destaque** própria, alternando entre
**vinho** e **verde**, para dar ritmo ao e-book. No HTML isso é feito por seção:
`<section class="pag" style="--accent:var(--vinho)">` (ou `var(--verde)`).
As divisórias de módulo usam fundo **verde** com título em **dourado**.

Contraste (AA): corpo `#37413b` sobre creme é alto; vinho `#8B2F4C` e verde
`#5E7D68` como títulos sobre creme têm contraste confortável.

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

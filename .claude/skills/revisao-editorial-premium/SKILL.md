---
name: revisao-editorial-premium
description: >-
  Revisão editorial premium de ebooks e PDFs com foco em LEGIBILIDADE e
  apresentação profissional. Use SEMPRE que o usuário pedir para revisar,
  formatar, diagramar, "deixar bonito", melhorar a leitura ou o visual de um
  ebook, apostila, PDF ou material digital — inclusive quando reclamar que "as
  letras/fontes estão pequenas", "as cores estão desproporcionais", "tem texto
  demais", "o conteúdo está achatado/espremido" ou "as imagens estão cortadas".
  Corrige tipografia, hierarquia de títulos, espaçamento, tamanho de fonte,
  paleta de cores, comprimento de parágrafos e margens, e gera um arquivo final
  premium (PDF pronto por padrão; HTML ou Word sob pedido). Vale mesmo quando o
  usuário não usa a palavra "skill" ou "editorial".
---

# Revisão Editorial Premium

Transforme um ebook confuso e cansativo de ler em um material **premium, leve e
profissional**. O objetivo não é só "corrigir erros": é fazer a leitura fluir.
Quem abre o material precisa sentir vontade de continuar.

## REGRA INEGOCIÁVEL: preservar 100% do conteúdo

Este material é um **infoproduto** — cada frase foi paga e pensada. Portanto:

- **Não remova nada.** Nenhuma frase, número, receita, dica ou detalhe pode
  sumir. Todo o texto original tem de continuar presente.
- **Não reescreva o sentido nem "melhore" as palavras.** Você não é revisor de
  texto; é diagramador. Mantenha a voz e as palavras da autora.
- **Não invente conteúdo novo** (nem exemplos, nem frases de preenchimento).
- O trabalho é **só visual**: reorganizar em títulos, parágrafos curtos, listas,
  destaques e imagens — vestindo o mesmo conteúdo, não trocando-o.

Como conciliar isso com "tem texto demais": a solução para um bloco denso
**nunca** é cortar. É **quebrar** — dividir em parágrafos curtos, transformar
sequências em listas, adicionar espaçamento e distribuir em mais páginas. O
conteúdo é o mesmo; só respira melhor.

Ao final, faça uma conferência: o texto revisado contém tudo o que estava no
original? Se qualquer trecho ficou de fora, volte e recoloque.

## Os 6 problemas que esta skill sempre resolve

O usuário costuma chegar com estas dores. Trate cada uma como um item de
checklist — não entregue o arquivo final enquanto todas não estiverem resolvidas.

1. **Fontes/letras pequenas** → corpo de texto nunca abaixo de 12pt (ideal 12–14pt).
2. **Cores desproporcionais** → paleta enxuta e harmônica, com contraste legível.
3. **Texto demais / blocos densos** → parágrafos curtos, listas, respiro visual.
4. **Falta de hierarquia** → títulos H1/H2/H3 bem definidos e consistentes.
5. **Conteúdo "achatado"/espremido** → espaçamento entre linhas e blocos generoso.
6. **Imagens cortadas** → imagens inteiras, dentro das margens, nunca estouradas.

## Fluxo de trabalho

### 1. Receber e ler o conteúdo original
- Se vier um **PDF**, extraia texto e imagens (use a skill `pdf` para isso).
- Se vier **Word/Docs**, extraia o conteúdo (use a skill `docx`).
- Se vier **texto/Markdown**, use direto.
- Preserve a intenção do autor. Você reorganiza e reveste o conteúdo — **não
  reescreve o sentido** nem inventa informação.

### 2. Reestruturar o texto (revisão editorial)
Aplique as regras de formatação a seguir. Este é o coração do trabalho.

### 3. Aplicar o design premium
Gere o arquivo final usando o template e as especificações visuais das
referências. **PDF é o formato padrão de entrega** (mais o HTML responsivo para
leitura no celular).

> **Identidade da marca (Bolo Rosa / Cacau Pitanga):** este material segue um
> manual de marca oficial. Antes de diagramar, leia
> `references/manual-marca-bolo-rosa.md` — ele traz a paleta exata (Vinho Cacau,
> Ocre Dourado, Verde Sálvia, Terracota, Verde Cacau, Creme, mais o **Rosé** e o
> **Azul** novos), as fontes (Playfair Display + Montserrat), as caixas de
> destaque e a adaptação para celular com fontes maiores. O CSS
> `assets/estilo-premium.css` já implementa tudo isso. Não use nenhuma cor, fonte
> ou estilo fora dessa identidade.

### 4. Conferir o checklist final
Antes de entregar, valide os 6 problemas acima e o checklist no fim deste arquivo.

## Regras de formatação (ESSENCIAL)

Estas regras foram pedidas explicitamente e são inegociáveis para a leitura.

- **Títulos bem definidos.** Use H1 para o título do capítulo, H2 para seções e
  H3 para subseções. Nunca pule níveis. O leitor precisa saber onde está só de
  bater o olho.
- **Espaçamento entre blocos.** Deixe respiro entre parágrafos, títulos, listas e
  imagens. Espaço em branco não é desperdício — é o que evita a sensação de
  "achatado".
- **Parágrafos curtos: no máximo 4 linhas.** Se um parágrafo passar disso, quebre
  em dois. Ideias longas viram vários parágrafos curtos.
- **Listas para facilitar a leitura.** Sempre que houver 3+ itens, passos ou
  exemplos em sequência, transforme em lista com marcadores ou numerada.
- **Destaque frases importantes com negrito.** Marque a ideia-chave de cada
  trecho em **negrito** — mas com parcimônia: se tudo é destaque, nada é.
- **Estrutura visual agradável.** Alterne texto, listas e imagens. Nenhuma página
  deve ser um paredão de texto corrido.
- **Muitos itens visuais.** O material precisa ser rico e convidativo: use selos,
  caixas de dica (💡) e atenção (⚠️), passos numerados em círculo, cartões,
  números em destaque e divisórias decorativas. O CSS já traz todos esses
  componentes prontos (`.selo`, `.dica`, `.atencao`, `.passos`, `.cartoes`,
  `.numerao`, `.divisoria`, `.abertura`) — use-os com generosidade.
- **Feito para o celular.** Coluna única, fontes grandes (corpo 16–18pt) e nada
  que exija zoom ou rolagem lateral. Ver a seção mobile-first das especificações.

Para os números exatos de fonte, entrelinha, margens, cores e regras de mobile,
leia `references/especificacoes-design.md` antes de gerar o arquivo.

## Como gerar o arquivo final

O caminho mais confiável e com melhor controle tipográfico é **HTML semântico +
CSS de impressão → PDF**:

1. Escreva o conteúdo já revisado em HTML semântico (`<h1>`, `<h2>`, `<p>`,
   `<ul>`, `<strong>`, `<figure>`).
2. Use o template `assets/estilo-premium.css` como folha de estilo (já traz
   fontes maiores, entrelinha generosa, paleta harmônica e imagens que nunca
   estouram a margem).
3. Converta com o script:

   ```bash
   python scripts/gerar_pdf.py entrada.html saida.pdf
   ```

   O script tenta WeasyPrint (melhor resultado) e cai para Playbook/Chromium se
   necessário. Se nenhum estiver disponível, ele explica como instalar e, no
   mínimo, entrega o HTML pronto para "Imprimir → Salvar como PDF".

Se o usuário preferir **Word editável**, use a skill `docx` aplicando os mesmos
tamanhos de fonte, estilos de título e espaçamento das especificações.

## Imagens: nunca cortadas, nunca esticadas

Imagem cortada é o erro que mais quebra a sensação "premium". Regras:

- Toda imagem entra com `max-width: 100%` — encaixa na largura útil da página.
- Nunca force altura fixa que distorça a proporção.
- Dê respiro (margem) acima e abaixo, e uma legenda curta quando ajudar.
- Se a imagem original chegou cortada/baixa resolução, avise o usuário em vez de
  entregar algo ruim — pergunte se ele tem o arquivo original.

## Checklist final (rode antes de entregar)

- [ ] Corpo de texto ≥ 12pt e confortável de ler.
- [ ] Títulos H1/H2/H3 consistentes e com destaque claro.
- [ ] Nenhum parágrafo com mais de 4 linhas.
- [ ] Sequências viraram listas.
- [ ] Frases-chave em negrito, sem exagero.
- [ ] Espaçamento generoso entre blocos (nada "achatado").
- [ ] Paleta enxuta (2–3 cores + neutros) e com bom contraste.
- [ ] Todas as imagens inteiras, dentro da margem, na proporção certa.
- [ ] Arquivo final gerado no formato pedido (PDF por padrão).

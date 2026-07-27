# Apresentação

`projeto-completo.html` é a fonte. O PDF é gerado a partir dela:

```
/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --disable-gpu --no-sandbox \
  --print-to-pdf="Cacau-Pitanga-Projeto-Completo.pdf" --no-pdf-header-footer \
  "file://$PWD/projeto-completo.html"
```

Edite o HTML, nunca o PDF. Os campos marcados como "a preencher" precisam dos números
reais antes de enviar a qualquer parceiro.

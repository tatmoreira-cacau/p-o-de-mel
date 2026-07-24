#!/usr/bin/env python3
"""
Gera um PDF premium a partir de um HTML já estilizado.

Uso:
    python gerar_pdf.py entrada.html saida.pdf

Estratégia (tenta em ordem, usa o primeiro que funcionar):
  1. WeasyPrint  — melhor controle tipográfico e de @page (recomendado).
  2. Chromium/Playwright — ótimo para HTML responsivo/mobile.
Se nenhum estiver disponível, explica como instalar e mantém o HTML,
que já pode ser aberto no navegador e salvo como PDF (Imprimir → Salvar como PDF).
"""
import sys
import os


def com_weasyprint(html_path, pdf_path):
    from weasyprint import HTML
    HTML(filename=html_path).write_pdf(pdf_path)
    return True


def com_chromium(html_path, pdf_path):
    # Chromium pagina melhor (grid/flex, break-inside) e carrega as fontes.
    # Playwright acha o binário sozinho via PLAYWRIGHT_BROWSERS_PATH.
    from playwright.sync_api import sync_playwright
    url = "file://" + os.path.abspath(html_path)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(1200)  # garante fontes carregadas
        page.pdf(path=pdf_path, print_background=True, prefer_css_page_size=True)
        browser.close()
    return True


def main():
    if len(sys.argv) != 3:
        print("Uso: python gerar_pdf.py entrada.html saida.pdf")
        sys.exit(1)
    html_path, pdf_path = sys.argv[1], sys.argv[2]

    # Chromium primeiro (melhor paginação); WeasyPrint como reserva.
    for nome, fn in (("Chromium", com_chromium), ("WeasyPrint", com_weasyprint)):
        try:
            fn(html_path, pdf_path)
            print(f"PDF gerado com {nome}: {pdf_path}")
            return
        except ImportError:
            continue
        except Exception as e:
            print(f"{nome} falhou: {e}")
            continue

    print(
        "Nenhum conversor disponível.\n"
        "Instale um destes:\n"
        "  pip install weasyprint\n"
        "  pip install playwright\n"
        f"Enquanto isso, o HTML pronto está em: {html_path}\n"
        "Abra-o no navegador e use Imprimir → Salvar como PDF."
    )
    sys.exit(2)


if __name__ == "__main__":
    main()

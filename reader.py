import fitz

def encontrar_assunto(pdf):
    processo = fitz.open(pdf)

    assunto = []
    palavras_chave = ['objeto', 'prazo']

    for page_n in range(processo.page_count):
        pagina = processo[page_n]
        texto = pagina.get_text()
        paragrafos = texto.split('\n')
        print(len(texto))

        for paragrafo in paragrafos:
            if any(palavra_enc in paragrafo.lower() for palavra_enc in palavras_chave):
                assunto.append(paragrafo)

    processo.close()

    return assunto

print(encontrar_assunto('ex01.pdf'))
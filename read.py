import PyPDF2

def extrair_paragrafos_com_palavras_chave(pdf_path, palavras_chave):
    paragrafos_encontrados = []

    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        
        for page in reader.pages:
            text = page.extract_text()
            for paragrafo in text.split('\n\n'):  # Supondo que os parágrafos estão separados por duas quebras de linha
                if any(palavra_chave in paragrafo for palavra_chave in palavras_chave):
                    paragrafos_encontrados.append(paragrafo)

    return paragrafos_encontrados

# Exemplo de uso
pdf_path = 'ex01.pdf'
palavras_chave = ['objeto', 'prazo']
paragrafos = extrair_paragrafos_com_palavras_chave(pdf_path, palavras_chave)

for paragrafo in paragrafos:
    print(paragrafo)

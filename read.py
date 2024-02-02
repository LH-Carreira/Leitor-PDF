import pytesseract
from pdf2image import convert_from_path

def extrair_texto_pdf_digitalizado(pdf_path):
    # Convertendo o PDF em imagens
    imagens = convert_from_path(pdf_path)
    
    texto_completo = ''
    
    for imagem in imagens:
        texto_imagem = pytesseract.image_to_string(imagem, lang='por')  
        texto_completo += texto_imagem
    
    return texto_completo

def encontrar_paragrafos_chave(texto, palavras_chave):
    paragrafos = texto.split('\n\n')  # Dividir o texto em parágrafos
    paragrafos_encontrados = []
    
    for paragrafo in paragrafos:
        for chave, palavra_chave in palavras_chave.items():
            if palavra_chave in paragrafo.lower():
                paragrafos_encontrados.append((chave, paragrafo))
    
    return paragrafos_encontrados

# Exemplo de uso
pdf_path = 'ex01.pdf'
texto_extraido = extrair_texto_pdf_digitalizado(pdf_path)
palavras_chave = {'Solicitando': 'ajuizada por ', 'Objeto': 'objeto a ', 'Prazo': 'solicito que sejam encaminhados'}
paragrafos_chave = encontrar_paragrafos_chave(texto_extraido, palavras_chave)

for i, (chave, paragrafo) in enumerate(paragrafos_chave, start=1):
    print(f"{chave} {i}:")
    print(paragrafo)
    indice_ultima_ocorrencia = paragrafo.lower().rindex(palavras_chave[chave])
    print(indice_ultima_ocorrencia)
    print("\n")


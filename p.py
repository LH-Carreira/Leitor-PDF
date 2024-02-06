import pytesseract
from pdf2image import convert_from_path

# Instale as bibliotecas necessárias:
# pip install pytesseract pdf2image

def extrair_texto_pdf_digitalizado(pdf_path):
    # Convertendo o PDF em imagens
    imagens = convert_from_path(pdf_path)
    
    texto_completo = ''
    
    for imagem in imagens:
        texto_imagem = pytesseract.image_to_string(imagem, lang='por')  # Pode ser necessário ajustar o idioma 'por' para o seu caso
        texto_completo += texto_imagem
    
    return texto_completo

# Exemplo de uso
pdf_path = 'ex02.pdf'
texto_extraido = extrair_texto_pdf_digitalizado(pdf_path)
print(texto_extraido)

import pandas as pd
import pytesseract
from pdf2image import convert_from_path

# Objeto Data Nome solicitante Prazo codigo Multa
df = pd.DataFrame(columns=['PROTOCOLO', 'DATA DE ENTRADA', 'ORGÃO EMISSOR', 'INTERESSADO', 
                           'NOME DO SERVIDOR OU INTERSSADO', 'ORIGEM', 'ASSUNTO', 'SUB-ASSUNTO', 
                           'TIPO A SER ATENDIDO', 'OBJETO', 'PRAZO DE ATENDIMENTO', 'SE HÁ MULTA', 
                           'STATUS', 'SETOR TRAMITADO', 'DATA DE SAÍDA', 'OBSERVAÇÃO', 'PRIORIDADE'])


def extrair_texto_pdf_digitalizado(pdf_path):
    # Convertendo o PDF em imagens
    imagens = convert_from_path(pdf_path)
    
    texto_completo = ''
    
    for imagem in imagens:
        texto_imagem = pytesseract.image_to_string(imagem, lang='por')  
        texto_completo += texto_imagem
    
    return texto_completo


pdf_path = 'ex02.pdf'
texto_extraido = extrair_texto_pdf_digitalizado(pdf_path)
palavras_chave = {'NOME DO SERVIDOR OU INTERSSADO': ['ajuizada por ', '(CPF'],
                   'OBJETO': ['objeto a ', '.'],
                    'PRAZO DE ATENDIMENTO': ['sejam encaminhados', 'dias']}

for chave in palavras_chave:
    print(f"{chave}:")
    primeira_ocorrencia = texto_extraido.lower().rindex(palavras_chave[chave][0]) + len(palavras_chave[chave][0])
    ultima_ocorrencia = texto_extraido.find(palavras_chave[chave][1], primeira_ocorrencia)

    if chave == 'PRAZO DE ATENDIMENTO':
        dado = texto_extraido[primeira_ocorrencia:ultima_ocorrencia + 4]
    else:
        dado = texto_extraido[primeira_ocorrencia:ultima_ocorrencia]

    print(dado)
    print("\n")

    # Adicionando ao DataFrame
    df[chave] = [dado]  # Você precisa passar uma lista para que cada valor seja atribuído a uma linha diferente

df.to_excel('xxx.xlsx', index=False)

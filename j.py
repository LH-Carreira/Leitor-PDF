palavras_chave = {'Solicitando': ['ajuizada por ', '(CPF'], 'Objeto': ['objeto a ', '.'], 'Prazo': ['solicito que sejam encaminhados', 'documentos']}

for chave, x in enumerate(palavras_chave, start=1):
    print(chave)
    print(palavras_chave[x][0])
    print(palavras_chave[x][1])
    # primeira_ocorrencia = texto_extraido.lower().rindex(palavras_chave[chave][0]) + len(palavras_chave[chave][0])
    # ultima_ocorrencia = texto_extraido.index(palavras_chave[chave][1])
    # dado = texto_extraido[primeira_ocorrencia:ultima_ocorrencia]
    # print(dado)
    print("\n")
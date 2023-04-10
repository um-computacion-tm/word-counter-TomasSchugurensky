def contar_palabras (text):
    frase = {}
    lista = text.lower().split()
    for frase in lista:
        if frase in frase:
            frase[frase] +=1
        else:
            frase[frase] =1
    resultado = frase 
    return resultado
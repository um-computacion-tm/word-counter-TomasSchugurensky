def contar_palabras (text):
    resultado = {}
    for word in text.split(''):
        lower_word = text.lower()
        if word in resultado:
            resultado[word.lower()] +=1
        else:
            resultado[word.lower()] =1
    return resultado
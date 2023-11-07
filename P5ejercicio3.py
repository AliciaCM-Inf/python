frase=input('Introdueix una frase: ')
#Los caracteres que no contamos como palabras de la frase
quitar = " ,;:.\n!\"'"
for caracter in quitar:
    frase = frase.replace(caracter,
                          " ")

frase = frase.lower()
palabras = frase.split(" ")

diccionario_frecuencias = {}
for palabra in palabras:
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1
    else:
        diccionario_frecuencias[palabra] = 1
        
for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]

print('Frecuencias = ',diccionario_frecuencias)

from collections import Counter

contador= Counter(palabras)
palabra_frecuente = contador.most_common()[0][0]
print('Palabra mas repetida : %s' % palabra_frecuente)





diccionario = {}
palabras =input('Introdui les paraules del diccionari: ')
palabras = palabras.lower()
for i in palabras.split(","):
    clave,valor = i.split(":")
    diccionario[clave] = valor
    
frase =input('Introduiu la frase a traduir: ')
frase = frase.lower()
for j in frase.split(' '):
    if j in diccionario:
        print(diccionario[j],end= ' ')
    else:
        print(j,end= ' ')

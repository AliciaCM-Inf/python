#Carga por teclado y crea una lista de numero enteros . Genera dos listas 1.Lista sin mayores de 10 2.Lista con mayores de 10:
lista=input('Entra una lista de valores separados por comas:')
lista=lista.split(',')
lista_mayores=[]
lista_menores=[]
for x in lista:
    if int (x) > 10:
         lista_mayores.append(x)
    else:
        lista_menores.append(x)

print ('Lista con mayores de 10: '+str(lista_mayores))
print ('Lista sin mayores de 10: '+str(lista_menores))

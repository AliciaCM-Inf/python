#este programa pide dos listas separadas por comas
#devuelve :Lista sesnse duplicats;Lista ordenada;Lista invertida

lista1=input('Entre una lista de valores separados por comas:')
lista2 =input("Entre una lista de valores separados por comas: ")

lista1=lista1.split(',')
lista2=lista2.split(',')
listacompleta=lista1+lista2

listasinduplicados = []
for x in listacompleta:
  if (x) not  in listasinduplicados:
    listasinduplicados.append(x)
print('Lista sin duplicados: '+str(listasinduplicados))
listasinduplicados.sort()
print('Lista ordenada: '+str(listasinduplicados))
listasinduplicados.reverse()
print('Lista inversa: '+str(listasinduplicados))










         


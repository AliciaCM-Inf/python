#este programa pide una lista de estaturas separadas por comas
#devuelve la media , personas mas altas de la media , personas mas bajas de la media
estaturas=input('Escribe una lista de estaturas separadas por comas: ')
estaturas=estaturas.split(',')
#bucle para pasarlo a float,tiene que ser un valor por valor 
estaturas_float=[]
for x in estaturas:
    estaturas_float.append(float(x))
print('Lista de estaturas: '+str(estaturas_float))
suma=0
for x in estaturas_float:
    suma=suma + x

media= suma/len(estaturas_float)
print('Media='+str (media))

(contadoraltas)=0
for x in estaturas_float :
    if x > media:
        contadoraltas += 1

print('Personas mas altas que la media: '+str(contadoraltas))

contadorbajas=0
for x in estaturas_float :
    if x < media:
        contadorbajas += 1
print('Personas mas bajas que la media: '+str(contadorbajas))

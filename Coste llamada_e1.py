#Este programa calcula el precio de llamada por precio a 5 centimos por minuto
def costellamada(tiempo):
    totalminutos=int(tiempo[0:2])*60+int(tiempo[3:5])
    coste=(totalminutos*0.05)+ 0.10
    return coste

tiempo=input('Temps de la trucada (HH:MM:SS): ')
print('Cost de la trucada: '+str(costellamada(tiempo)))




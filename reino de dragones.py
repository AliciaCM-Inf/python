import random
import time

def mostrarIntroduccion():
    print('Estás en una tierra llena de dragones. Frente a tí')
    print('hay dos cuevas. En una de ellas, el dragon es generoso y')
    print('amigable y compartirá su tesoro contigo. El otro dragón')
    print('es codicioso y esta hambriento, y te devorará inmediatamente.')
    print()

def elegirCueva():
    cueva = ''
    while cueva != '1' and cueva != '2':
        print('A qué cueva quieres entrar? (1 o 2)')
        cueva= input()

    return cueva

def explorarCueva(cuevaElegida):
    print('Te aproximas a la cueva....')
    time.sleep(2)
    print('Es oscura y espeluznante....')
    time.sleep(2)
    print('¡Un gran dragon aparece subitamente frente a tí!Abre sus fauces')
    print()
    time.sleep(2)

    cuevaAmigable = random.randint (1,2)

    if cuevaElegida == str(cuevaAmigable):
        print('¡Te regala su tesoro!')
    else:
        print('¡Te engulle de un bocado!')

jugarDeNuevo = 'si'
while jugarDeNuevo == 'si' or jugarDeNuevo == 's':

    mostrarIntroduccion()

    numeroDeCueva = elegirCueva()

    explorarCueva(numeroDeCueva)

    print('¿Quieres jugar de nuevo? (si o no)')
    jugarDeNuevo = input()

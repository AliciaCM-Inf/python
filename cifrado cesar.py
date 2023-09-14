#cifrado cesar

TAM_MAX_CLAVE = 25

def obtenerModo():
    while True:
        print('¿Deseas encriptar o desencriptar un mensaje?')
        modo = input ().lower()
        if modo == 'encriptar' or modo == 'e' or modo == 'desencriptar' or modo =='d':
            return modo
        else:
            print('Ingresa "encriptar" o "e" o "desencriptar" o "d"')
            
def obtenerMensaje():
    print('Ingresa tu mensaje:')
    return input ()

def obtenerClave():
    clave = 0
    while True:
        print ('Ingresa el número de clave (1-'+ str(TAM_MAX_CLAVE)+')')
        clave= int(input ())
        if (clave >= 1 and clave <= TAM_MAX_CLAVE):
            return clave

def obtenerMensajeTraducido(modo,mensaje,clave):

    letras = 'abcdefghijklmnopqrstuvwxyz'

    if modo [0] == 'd':
        clave= -clave

    traduccion = ''

    for letra in mensaje:

        posicion_letra = letras.find(letra.lower())

        if posicion_letra != -1:
            letra_traducida = letras [(posicion_letra + clave) % len (letras)]
            if letra.isupper():
                letra_traducida = letra_traducida.upper()
            traduccion += letra_traducida
        else:
            traduccion += letra

    return traduccion

modo = obtenerModo()
mensaje = obtenerMensaje()
clave = obtenerClave()

print('Tu texto traducido es :')
print(obtenerMensajeTraducido(modo,mensaje,clave))
    

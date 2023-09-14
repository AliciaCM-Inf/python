#El programa dice si un año es bisiesto o no

n =int(input('Introduce el año:'))

if n % 4 != 0:
    print('El año ,',n,'no es bisiesto.')

if n % 4 == 0:
    print('El año,',n,' si es bisiesto')

    
#el simbolo % es un operador de modulo , devuelve la division ,del lado izquierdo y derecho. Se usa para conseguir el resultado de una division

    

#programa que verifica si una matricua es valida o no
#No acepta "A" "E" "I" "O" "U" "Ñ" "Q"
#La matricula se contrsuye por 4 numeros y 3 letras


def valormatricula(matricula):
    variable= 'bcdfghjklmnprstvwxyz'
    numeros= matricula[:4]
    variable= matricula[4:]
    if not numeros.isdigit():
        print ('La matricula no es valida')
    for variable  in matricula:
        if len(matricula)== 7:
            print('La matricula es valida')
            break
    else:
        print('La matricula no es valida')

matricula =input('Introdueix la matricula:')
(valormatricula(matricula))


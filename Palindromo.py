#este programa devuelve si es un palindromo , o una frase o palabrao un numero
#Declarando variables
igual,aux = 0,0
#soliciar datos tanto numeros como letras
frase= input('Introduce una frase:')
#bucle for y reversed para aplicar los parametros del palindromo
for ind in reversed(range(0, len(frase))):
    if frase [ind].lower() == frase [aux].lower():
        igual += 1
    aux += 1
#condiciono con len
if len(frase)== igual:
    print("Es palindromo")

else:
    print("No es palindromo")

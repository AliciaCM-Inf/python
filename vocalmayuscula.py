#Programa que pide una frase y una vocal para mostrar la misma frase con la vocal en mayuscula
#definir funcion
#upper convierte en mayusculas(que es lo que queremos)
texto = input("Introduce un texto: ")
vocal = input("Introduce una vocal :  ")
print(texto.replace(vocal, vocal.upper()))


#Este programa basico cuenta cuantas vocales hay en una frase
def totaldevocales(letras):
	contador = 0
	for letra in texto:
		if letra.lower() in "aeiou":
			contador += 1
	return contador

letras = 'aeiou'   
texto= input('Introduce un texto:')
print("El texto introducido tiene",(totaldevocales(letras)),"vocales")

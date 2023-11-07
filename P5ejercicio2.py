#calcula el precio de la fruta por kilo y si hay o no en la lista 
tipo=input('Que fruta quieres?')
cantidad=input('Cuantos kilos ?')

frutas=[{"Fruta":"platano","Precio":2.35},
        {"Fruta":"manzana","Precio":2.80},
        {"Fruta":"pera","Precio":1.85},
        {"Fruta":"naranja","Precio":1.70},
        ]

precio = 0
pr = 0
for x in frutas :
    if x ["Fruta"]== tipo:
        precio=eval(cantidad)*x["Precio"]
        print('El precio es igual a ',precio,'€')
        pr = 1

if pr ==0:
    print('La fruta seleccionada no esta en la lista')
   
        


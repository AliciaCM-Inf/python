#pide nombre , edad, correo y telefono y luego da un registro con todo.
Nombre=input('Nombre: ')
Edad=input('Edad: ')
Direccion=input('Dirección: ')
Telefono=input('Telefono:')
usuari = {'Nombre': Nombre,'Edad': Edad,'Direccion':Direccion,'Telefono':Telefono}
print ('El usuario',usuari["Nombre"],'tiene',usuari["Edad"],'años, vive en',usuari["Direccion"],'y su numero de telefono es ',usuari["Telefono"])

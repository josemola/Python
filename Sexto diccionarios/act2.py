nombre = input("Dame tu nombre: ")
edad  = input("Dame tu edad: ")
direccion = input("Dame tu direccion: ")
telefono = input("Dame tu telefono: ")
diccionario={'nombre': nombre,'edad': edad,'direccion': direccion, 'telefono' : telefono}
print (diccionario['nombre'] + " tiene " + diccionario['edad'] + " años, vive en " + diccionario['direccion'] + " y su número de teléfono es " + diccionario['telefono'])
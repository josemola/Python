frase="nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
clientes={}

filas = frase.split("\n")

for i in range(1, len(filas)):
    datos_fila = filas[i].split(";")
    nif = datos_fila[0]
    nombre = datos_fila[1]
    email = datos_fila[2]
    telefono = datos_fila[3]
    descuento = datos_fila[4]
    
    datos = {"nombre": nombre,
             "email": email,
             "teléfono": telefono,
             "descuento": descuento}
    
    clientes[nif] = datos

print(clientes)



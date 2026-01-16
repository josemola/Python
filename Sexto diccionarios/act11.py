frase="nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
clientes={}
x=1
a=0

print(len(frase.split(";")))

while x < len(frase):
    nif= print(frase.split(";")[5+a])
    nombre= print(frase.split(";")[6+a])
    email= print(frase.split(";")[7+a])
    telefono= print(frase.split(";")[8+a])
    descuento= print(frase.split(";")[9+a])

    datos={"nombre":nombre,
    "email":email,
    "teléfono":telefono,
    "descuento":descuento,}
    x=x+1
    a=a+5
    clientes[nif]=datos



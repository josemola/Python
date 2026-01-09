diccionario={}
termina = "no"
total=0
while termina != "si":
    articulo=input("Dame el nombre del artículo: ")
    precio=float(input("Dame el precio: "))
    diccionario[articulo]=precio
    print(diccionario)
    termina=input("¿Has terminado? ")

for articulo, precio in diccionario.items():
    print(f"Artículo {articulo}  {precio} precio")
    total= total+precio

print("Total: ", total," coste")
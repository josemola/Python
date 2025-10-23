producto=input("Introduce el nombre del producto: ")
precio=float(input("Introduce el precio del producto: "))
unidades=float(input("Introduce las unidades del producto: "))
total=(precio)*(unidades)
totalA=f"{total:011.2f}"
precioA=f"{precio:09.2f}"
print("Tenemos el producto",producto, "que cuesta", precioA, "euros y tenemos", unidades, "unidades, el coste total es de", totalA, "euros")
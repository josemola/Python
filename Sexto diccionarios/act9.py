diccionario={}
numero=1
x=0

while x != 3:
    print("Estas son tus facturas: ")
    print(diccionario)

    print("1 añadir")
    print("2 pagar")
    print("3 terminar")
    x=int(input("SELECCIONA UN NÚMERO: "))

    if x==1:
        coste= int(input("Introduce el costo de tú factura: "))
        diccionario[numero]=coste
        numero=numero+1
    elif x==2:
        numeroborrar= int(input("Introduce el costo de tú factura: "))
        if numeroborrar in diccionario:
            del  diccionario[numeroborrar]
        else:
            print("Este número no existe")
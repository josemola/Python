diccionario={}
termina = "no"
while termina != "si":
    clase=input("Dame una clase a la que pertenece tu dato: ")
    info=input("Dame la información de esa clase de dato: ")
    termina=input("¿Has terminado? ")
    diccionario[clase]=info
    print(diccionario)
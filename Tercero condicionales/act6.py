sexo=input("Introduce tu sexo (hombre/mujer): ")
nombre=input("Introduce tu nombre: ")
if sexo=="mujer" and nombre.lower()[0] <= "m" or sexo=="hombre" and nombre.lower()[0] >= "n":
    print("perteneces al grupo A")
else:
    print ("perteneces al grupo B")  
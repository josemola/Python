puntos=float(input("Introduce tu puntucación: "))
if puntos==0.4:
    print("",round(2400*0.4,2),"euros")
elif puntos>=0.6:
    print("",round(2400*puntos,2),"euros")
else:
    print("No tienes bonus")
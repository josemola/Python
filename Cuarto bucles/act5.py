inversion=float(input("Dame una cantidad a invertir: "))
interes=float(input("Dame el interés porcentual anual: "))
anios=int(input("Dame el número de años: "))
ganancias=0
x=0
while anios>0:
    x=x+1
    ganancias=ganancias+((ganancias+inversion)*interes/100)
    print("Cantidad ganada después de",x,"años:",ganancias)
    anios-=1
print("Cantidad total de dinero ganado + invertido después de",x,"años:",inversion+ganancias)
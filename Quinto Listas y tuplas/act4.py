ganadores=[]
x=0
while x!=3:
    num=int(input("Introduce el numero ganador: "))
    ganadores.append(num)
    x=x+1
ganadores.sort()
print("Los números ganadores ordenados de menor a mayor son:", ganadores)
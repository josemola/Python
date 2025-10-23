entero=int(input("Dame un número entero: "))
contador=0
print("Números impares desde 1 hasta",entero)
while contador<=entero:
    if(contador%2!=0):
        print(contador)
    contador+=1
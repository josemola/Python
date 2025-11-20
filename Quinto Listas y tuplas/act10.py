lista=[50,75,46,22,80,65,8]
x=0
mayor=0
menor=1000000000
while x<len(lista):
    if lista[x]>mayor:
        mayor=lista[x]
    elif lista[x]<menor:
        menor=lista[x]
    x=x+1

print ("El valor mayor es: ",mayor," y el menor es ",menor)
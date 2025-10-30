num=int(input("Dame un número entero positivo: "))
primo=0
x=1
while x<=num:
    if num%x==0:
        primo=primo+1
    x=1+x
if primo>2:
    print("No es primo")
else:
    print("Es primo")
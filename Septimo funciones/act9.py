num1=int(input("Dime un numero: "))
num2=int(input("Dime otro numero: "))

#Explicación porque me he quedado loco, porque yo lo hacía de otra manera:
#a=24 y b=18 entonces a%b=6 y ahora se cambian a=18 y b=6
#a%b=0 entonces al ser 0 sabemos que el Mínimo común divisor es 6
def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calcular_mcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // calcular_mcd(a, b)

print(f"El MCD de {num1} y {num2} es: {calcular_mcd(num1, num2)}")
print(f"El MCM de {num1} y {num2} es: {calcular_mcm(num1, num2)}")
numero = int(input("Dime un numero positivo: "))

def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total = total * i
    return total

resultado = factorial(numero)
print(resultado)
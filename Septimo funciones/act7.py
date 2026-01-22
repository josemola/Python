def cuadrado(lista):
    total = []
    for numero in lista:
        num = numero ** 2
        total.append(num)
    return total

print(cuadrado([1, 2, 2, 3, 3, 5]))
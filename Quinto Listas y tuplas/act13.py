datos = input("Dame números separados por comas: ")
lista = [int(t.strip()) for t in datos.split(",")]
x = 0
suma = 0
while x < len(lista):
    suma = suma + lista[x]
    x = x + 1

media=suma / len(lista)
print(media, "Esta es la media")
print(lista)

sumacuadrados = 0
x = 0
while x < len(lista):
    a = lista[x] - media
    s = a ** 2
    sumacuadrados = sumacuadrados + s
    x = x + 1

desviatipica = (sumacuadrados / len(lista)) ** 0.5
print(desviatipica, "Esta es la desviación típica")

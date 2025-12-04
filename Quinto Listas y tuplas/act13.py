datos = input("Dame números separados por comas: ")
lista = [int(t.strip()) for t in datos.split(",")]
x = 0
suma = 0
while x < len(lista):
    suma = suma + lista[x]
    x = x + 1

    a=lista[x]-lista[x+1]
    s=a**2
    print(s)
    
print(suma)
media=suma / len(lista)
print(media, "Esta es la media")
print(lista)

desviatipica= 1
print(desviatipica)
print(suma)

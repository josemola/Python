palabra=str(input("Dime una palabra: "))
if palabra == palabra[::-1]:
    print ("La palabra ",palabra," es un palíndromo")
else:
    print ("La palabra ",palabra," no es un palíndromo")
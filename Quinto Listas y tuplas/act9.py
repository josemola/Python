vocales=["a","e","i","o","u"]
palabra=input("Dime una palabra y te diré las vocales: ")
x=0
cuenta=0
while x<len(palabra):
    if palabra[x] in vocales:
        cuenta=cuenta+1
    x=x+1
print ("Hay", cuenta,"vocales")
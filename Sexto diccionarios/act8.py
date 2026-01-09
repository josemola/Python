diccionario={}
termina="no"
x=0
while termina != "si":
    palabra=input("Dame una palabra en 'español:inglés': ")
    termina=input("¿Has terminado? ")
    diccionario[palabra.split(":")[0]]=palabra.split(":")[1]

frase=input("Dame una frase en español: ")

while x != 10:
    if frase.split(" ")[x]() in diccionario:
        print(diccionario[frase.split(" ")[x]()])
    x=x+1
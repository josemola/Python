frase=str(input("Dame una frase: "))
letra=str(input("Dame una letra: "))
x=len(frase)
cuantas=0
while x>0:
    if frase[x-1]==letra:
        cuantas=cuantas+1
    x=x-1
print("La letra",letra.upper(),"aparece",cuantas,"veces en la frase")
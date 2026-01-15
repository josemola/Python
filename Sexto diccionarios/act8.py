diccionario={}
palabra=input("Dame una palabra en 'español':'inglés' separadas por comas: ")
x=0
for par in palabra.split(','):
    esp, eng = par.split(':')
    diccionario[esp.strip()] = eng.strip()

frase=input("Dame una frase en español: ")

frasePalabras = frase.split()
resultado = []

for aaa in frasePalabras:
    traduccion = diccionario.get(aaa, aaa)
    resultado.append(traduccion)

print("La frase se traduce a: ", " ".join(resultado))
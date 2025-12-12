diccionario={'Euro':'€','Dollar':'$','Yen':'¥'}
divisa=input("Dime una divisa: ")
if divisa.title() in diccionario:
    print(diccionario[divisa.title()])
else:
    print("Eso no es válido")
diccionario={'Plátano': 1.35,'Manzana': 0.80,'Pera': 0.85, 'Naranja' : 0.70}
nombre = input("Dime una fruta: ")
if nombre.title() in diccionario:
    print(diccionario[nombre.title()])
else :
    print ("La fruta no existe")
diccionario={'Plátano': 1.35,'Manzana': 0.80,'Pera': 0.85, 'Naranja' : 0.70}
nombre = input("Dime una fruta: ")
kgs = float(input("Dime cuantos kilos quieres: "))
if nombre.title() in diccionario:
    print("El precio de ", nombre, " es ", float(diccionario[nombre.title()])*kgs)
else :
    print ("La fruta no existe")
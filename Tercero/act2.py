contrasena=input("Introduce la contraseña: ")
cual=input("¿Cuál era tú contraseña?: ")
if cual.lower()==contrasena.lower():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
diccionario = {"Matemáticas":6, "Física":4, "Química":5}
total= 0
for asignatura, creditos in diccionario.items():
    print(f"{asignatura} tiene {creditos} creditos")
    total= total+creditos

print("En total tienes: ", total," créditos")
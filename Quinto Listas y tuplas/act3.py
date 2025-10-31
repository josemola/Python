asignaturas=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas=[]
x=0
y=0
while x<5:
    a=asignaturas[x]

    nota=input("¿Qué has sacado en "+ a+ "?: ")
    notas.append(nota)
    x=x+1
while y<5:
    a=asignaturas[y]
    z=notas[y]
    print("En asignatura ", a, " has sacado ", z)
    y=y+1
asignaturas=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas=[]
x=0
n=0
cuantas=len(asignaturas)
repite=0
while x<cuantas:
    a=asignaturas[x]
    nota=int(input("¿Qué has sacado en "+ a+ "?: "))
    if nota>=5:
        asignaturas.remove(a)
        cuantas=len(asignaturas)
    else:
        repite=repite+1
        x=x+1
if repite>0:
    print("Debes repetir: ")
    while n!=repite:
        print(asignaturas[n])
        n=n+1
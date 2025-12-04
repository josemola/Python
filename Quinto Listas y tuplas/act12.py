matriz1=[
    [1,3,3],
    [4,5,2]
]
matriz2=[
    [4,2],
    [5,7],
    [5,7]
]
#No se puede realizar porque faltan las matrices, lo de abajo iba a calcular cualquier matriz
#pero como no se me pide eso, no lo he terminado.
# print(matriz1[0][1]) = 3 el del centro
# print (len(matriz1)) = 2 altura de la matriz
# print (len(matriz1[0])) = 3 ancho de la matriz

suma=0
res=[[]]
x = 0
y = 0
xa=0
ya= 0
contar=0
fila=0
while contar != len(matriz1) : # calcula por fila en este caso 2
    while xa != len(matriz2[0]) : # calcula la columna de la 2ª en este caso 2
        while x < len(matriz1[0]) :  # recorre todos los elementos k (0..cols-1)
            pt1=matriz1[y][x]*matriz2[x][xa]  # matriz1[row][k] * matriz2[k][col]
            suma=pt1+suma
            x=x+1
        x=0
        ya=0
        res[contar].append(suma)
        xa=xa+1
        suma=0
    if contar+1 != len(matriz1):
        res.append([])
    y=y+1
    xa=0
    contar=contar+1

for fila in res:
    print(fila)
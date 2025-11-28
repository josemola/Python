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
res=[]
x = 0
y = 0
xa=0
ya= 0
contar=0
fila=0
print(len(matriz1[1]))

while contar != len(matriz1) :
    while x != len(matriz1[1]) :
        while x != len(matriz1[1]) :
            pt1=matriz1[x][y]*matriz2[xa][ya]
            suma=pt1+suma
            x=x+1
            ya=ya+1
    res=suma
    suma=0
    x=0
    ya=0
    xa=xa+1
xa=0
contar=contar+1



    y=0
    xa=0
    pt1=matriz1[x][y]*matriz2[xa][ya]
    y=y+1
    xa=xa+1
    pt2=matriz1[x][y]*matriz2[xa][ya]
    resultado=pt1+pt2
    if ya == 0 :
        ya=ya+1
    else:
        ya = 0
        x = x+1
    anadir=res.append(resultado[fila][contar])
    contar=contar+1
    if contar == len(matriz1):
        fila=fila+1
    print (resultado)
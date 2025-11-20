matriz1=[
    [1,3],
    [4,5]
]
matriz2=[
    [4,2],
    [5,7]
]
res=[]
x = 0
y = 0
xa=0
ya= 0
contar=0
fila=0
while contar != len(matriz1)*2 :
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
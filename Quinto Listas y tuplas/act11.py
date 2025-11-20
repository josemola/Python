vec1=[1,2,3]
vec2=[-1,0,2]
x=0
z=0
while x != len(vec1):
    y=vec1[x]*vec2[x]
    z=z+y
    x=x+1
print ("El producto escalar es: ", z)
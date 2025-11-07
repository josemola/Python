abecedario=[ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cuantas=len(abecedario)
val=2
while val<cuantas:
    zz=abecedario[val]
    abecedario.remove(zz)
    val=val+2
    cuantas=len(abecedario)
print (abecedario)
def circulo(rad):
    total=3.1416*(rad^2)
    return total

def cilindro(r,h):
    resultado=3.1416*(r**2)*h
    return resultado

print("El area del circulo es: ",circulo(10))
print("El volumen del cilindro es: ", cilindro(5,3))
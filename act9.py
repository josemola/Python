invierte = float(input("Dime una cantidad a invertir: "))
intereses = float(input("Dime el interes anual: "))
años = float(input("Dime los años de inversión: "))
interes = float(intereses) / 100
Resultado= interes * invierte * años
print ("Has generado " + str(Resultado))
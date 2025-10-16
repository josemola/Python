renta=float(input("Introduce tu renta anual: "))
if renta<10000:
    print("Tipo impositivo del 5%, debes pagar",round(renta*0.05,2),"euros")
elif renta>10000:
    print("Tipo impositivo del 5%, debes pagar",round(renta*0.15,2),"euros")
elif renta>20000:
    print("Tipo impositivo del 20%, debes pagar",round(renta*0.20,2),"euros")
elif renta>35000:
    print("Tipo impositivo del 30%, debes pagar",round(renta*0.30,2),"euros")
elif renta>60000:
    print("Tipo impositivo del 45%, debes pagar",round(renta*0.45,2),"euros")
Edad=input("Introduce tu edad: ")
ingresos=input("Introduce tus ingresos mensuales: ")
if int(Edad)<16 or int(ingresos)<1000:
    print("No debes tributar")
else:
    print("Debes tributar")
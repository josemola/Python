pizza=input("Hola ¿Quieres una pizza vegetariana?: ")
if pizza.lower=="si":
    print("Los ingredientes son: Pimiento y tofu")
    ingredientes=input("Elige un ingrediente:")
else:
    print("Los ingredientes son: Peperoni, jamón y salmón")
    ingredientes=input("Elige un ingrediente: ")
print("Tu pizza no vegetariana lleva: "+ingredientes)
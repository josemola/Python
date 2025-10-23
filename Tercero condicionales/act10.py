pizza=input("Hola ¿Quieres una pizza vegetariana?: ")
if pizza.lower()=="si":
    print("Los ingredientes son: Pimiento y tofu")
    ingredientes=input("Elige un ingrediente con una P o T:")
    if ingredientes.lower()=="p":
        ingredientes="Mozzarella, Tomate y Pimiento"
    elif ingredientes.lower()=="t":
        ingredientes="Mozzarella, Tomate y Tofu"
    else:
        ingredientes="Mozzarella y Tomate"
    print("Tu pizza vegetariana lleva: "+ingredientes)
else:
    print("Los ingredientes son: Peperoni, jamón y salmón")
    ingredientes=input("Elige un ingrediente con una P, J o S: ")
    if ingredientes.lower()=="p":
        ingredientes="Mozzarella, Tomate y Peperoni"
    elif ingredientes.lower()=="j":
        ingredientes="Mozzarella, Tomate y Jamón"
    elif ingredientes.lower()=="s":
        ingredientes="Mozzarella, Tomate y Salmón"
    else:
        ingredientes="Mozzarella y Tomate"
    print("Tu pizza no vegetariana lleva: "+ingredientes)
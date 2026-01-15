cliente={}

x=0
while x!=6:
    print ("1 Añadir cliente")
    print ("2 Eliminar cliente")
    print ("3 Mostrar cliente")
    print ("4 Listar todos")
    print ("5 Listar preferentes")
    print ("6 Salir")
    x= int(input("Selecciona un número: "))

    if x==1:
        nif= str(input("NIF de tú cliente: "))
        nombre= str(input("Nombre de tú cliente: "))
        direccion= str(input("Direccion de tú cliente: "))
        telefono= str(input("Teléfono de tú cliente: "))
        correo= str(input("Correo de tú cliente: "))
        preferencia= str(input("Preferencia de tú cliente con True/False: "))

        datos={"nombre":nombre,
        "direccion":direccion,
        "telefono":telefono,
        "correo":correo,
        "preferencia":preferencia}

        cliente[nif]=datos

    elif x==2:
        clienteborrar= str(input("Introduce el NIF de tú cliente: "))
        if clienteborrar in cliente:
            del  cliente[clienteborrar]
            
        else:
            print("Este nif no existe")
    
    elif x==3:
        clientebuscar= str(input("Introduce el NIF de tú cliente: "))
        if clientebuscar in cliente:
            print(cliente[clientebuscar])

        else:
            print("Este nif no existe")

    elif x==4:
        print("Estos son los clientes: ")
        for nifs, datoss in cliente.items():
            print(f"NIF: {nifs} -Nombre: {datos['nombre']}")

    elif x==5:
        #ARREGLAR
        print("Clientes preferentes: ")
        for nifs, datoss in cliente.items():
            if datoss['preferente']=="True":
                print(f"NIF: {nif} - Nombre: {datoss['nombre']}")


    
       
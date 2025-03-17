while True:
    print("Menu de opciones")
    print("1- Alta de productos")
    print("2- lista de productos")
    print("3_ salir")
    opcion = input("\ningresa la opcion que  desee: ").lower()

    if opcion == 1:
        # blose de codigo de alta
        nombreProducto = input("Nombre de producto: ")
        cantidadProducto = int(input("\nCantidad e producto: "))
        print("Producto en alta")

    elif opcion == 2:
        # bloque de codigo lista
        print("\nLista de productos")

    elif opcion == 3:
        print("\nSaliendo..")
        break
    else:
        print("Opcion no valida")

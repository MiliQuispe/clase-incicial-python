from funcionesDeProductos import *
from funcionesBaseDeDatos import crearLaTabla

"""Funciones de productos """


def menu():

    print(
        "=========Menu===========\n"
        "1- Registrar producto\n"
        "2- Visualizar productos\n"
        "3- Actualizar producto\n"
        "4- Eliminar producto\n"
        "5- Buscar producto\n"
        "6- Repotar bajo stock\n"
        "7- Salir\n"
    )
    opcion = int(input("Ingrese la opcion que desee: "))
    return opcion


def main():

    crearLaTabla()

    while True:
        opcion = menu()

        if opcion == 1:
            registrarProducto()
        elif opcion == 2:
            visualizarProductos()
        elif opcion == 3:
            actualizarProducto()
        elif opcion == 4:
            eliminarProducto()
        elif opcion == 5:
            buscarProducto()
        elif opcion == 6:
            reportarBajoStock()
        elif opcion == 7:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida")


main()

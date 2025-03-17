from funcionesBaseDeDatos import *
from funcionesDeValidacion import *


def registrarProducto():

    print("INGRESAR PRODUCTO")

    # ingresar productor por teclado
    print("\nIngrese datos del producto\n")

    # validar que nombre no sea vacia
    nombre = validarNombre()

    descripcion = input("Ingrese la descripcion del producto: ")

    # validar que categoria no sea vacia
    categoria = validarCategoria()

    # validar la cantidad
    cantidad = validarCantidad()

    # validar el precio
    precio = float(input("Ingrese el precio del producto: "))

    # crear el diccionario
    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
    }

    # guardar el producto en la base de datos
    print("\n", producto)
    insertarProductoEnTabla(producto)
    print("\nRegistro insertado exitosamente")


def visualizarProductos():

    # Obtener todos los productos de la base de datos
    print("\nVER PRODUCTOS\n")
    listaProductos = obtenerProductosDeLaTabla()

    # verificar si la lista esta vacia
    if not listaProductos:
        print("\nNo hay productos registrados")
    else:
        # mostrar los productos
        for producto in listaProductos:
            print(
                f"{producto[0]}, {producto[1]}, {producto[2]}, {producto[3]}, {producto[4]}, {producto[5]}"
            )
            print("\n")


def actualizarProducto():

    # ingresar el id y la cantida nueva del producto a actualizar
    print("ACTUALIZAR PRODUCTO")
    print("\nIngrese datos del producto a actualizar\n")
    id = int(input("Ingrese el id:\t"))
    cantidadNueva = int(input("Ingrese la nueva cantidad:\t"))

    # actualizar el producto en la base de datos
    actualizarProductoDeLaTabla(id, cantidadNueva)
    print("\nRegistro actualizado exitosamente\n")


def eliminarProducto():

    # ingresar el id del producto a eliminar
    print("\nELIMINAR PRODUCTO\n")
    id = int(input("Ingrese el id del producto a eliminar: "))

    # eliminar el producto de la base de datos
    eliminarProductoDeLatabla(id)
    print("\nRegistro eliminado exitosamente\n")


def buscarProducto():

    # buscar el producto en la base de datos
    print("\nBUSCAR PRODUCTO\n")
    id = int(input("Ingrese el id del producto a buscar: \n"))

    # obtener el producto de la base de datos
    producto = buscarProductoDeLaTabla(id)

    # verificar si el producto existe
    if producto:
        print(
            f"{producto[0]}, {producto[1]}, {producto[2]}, {producto[3]}, {producto[4]}, {producto[5]}"
        )
    else:
        print("\nNo hay productos con ese id\n")


def reportarBajoStock():

    # se ingresa la cantidad minima para reportar
    print("\nREPORTE DE BAJO STOCK\n")
    condicion = input("Ingrese la condicion para el reporte :\t")

    # obtiene los productos con la condicion ingresada
    listaReporte = repotarBajoStockDeLaTabla(condicion)

    # verificar si hay productos con la condicion ingresada
    if not listaReporte:
        print("\nNo hay productos con ese id")
    else:
        for producto in listaReporte:
            print(
                f"{producto[0]}, {producto[1]}, {producto[2]}, {producto[3]}, {producto[4]}, {producto[5]}\n"
            )

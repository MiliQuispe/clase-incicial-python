def validarNombre():

    while True:

        nombre = input("Ingrese su nombre: ")

        if nombre == "":
            print("El nombre no puede estar vacío")
        else:
            return nombre


def validarCategoria():
    while True:
        categoria = input("Ingrese la categoria: ")
        if categoria == "":
            print("La categoria no puede estar vacía")
        else:
            return categoria


def validarCantidad():
    while True:
        cantidad = input("Ingrese la cantidad: ")
        if cantidad:
            try:
                cantidad = int(cantidad)
                return cantidad
            except ValueError:
                print("La cantidad debe ser un número entero")
        else:
            print("La cantidad no puede estar vacía")


def validarPrecio():
    while True:
        precio = input("Ingrese el precio: ")
        if precio:
            try:
                precio = float(precio)
                return precio
            except ValueError:
                print("El precio debe ser un número decimal")
            else:
                print("El precio no puede estar vacío")

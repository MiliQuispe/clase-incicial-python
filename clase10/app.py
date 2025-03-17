# Lista para almacenar los productos
productos = []
diccionarioProducto = {}


# Función principal para el sistema de inventario (NO ELIMINAR)
def main():
    # AQUÍ PUEDES COMENZAR A DESARROLLAR LA SOLUCIÓN
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Salir")

        opcion = (int)(input("\nElija una opcion:\t"))

        if opcion == 1:
            nombre = input("\nIngrese el nombre del producto:\t")
            stock = int(input("\nIngrese la cantidad en stock del producto:\t"))

            # agregar el producto
            # productos.append([nombre, stock])
            diccionarioProducto = {"nombre": nombre, "stock": stock}
            productos.append(diccionarioProducto)
            print("Producto agregado\n")

        elif opcion == 2:

            # for indice in productos:
            # print(f"Nombre {productos[0]} stock {productos[1]}")

            # for indice in range(len (productos)):

            if len(productos) > 0:
                # for indice, producto in enumerate(productos):
                # print(f"{indice} Nombre: {producto[0]} Stock: {producto[1]}")
                # print(f"{indice} Nombre: {producto["nombre"]} Stock: {producto["stock"]}")

                for producto in productos:
                    print(
                        f" Nombre: {producto.get('nombre')} Stock: {producto['stock']}"
                    )

            else:
                print("\nNo hay productos")

        elif opcion == 3:
            print("\nSaliendo..")
            break

        else:
            print("\nOpcion incorrecta")


# Ejecución de la función main() - (NO ELIMINAR)
if __name__ == "__main__":
    main()

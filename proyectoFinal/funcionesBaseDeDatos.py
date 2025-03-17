import sqlite3

"""funciones para la base de datos """

ruta = r"C:\Users\Milagros quispe\Documents\clases\proyectoFinal\inventario.db"


def crearLaTabla():
    # Conectarse o crear la base de datos
    conexion = sqlite3.connect(ruta)

    # crear un puntero o cursor a la base de datos (funciona como un  puntero a file en archivos en c?)
    punteroCursor = conexion.cursor()

    # ejecutar una consulta
    punteroCursor.execute(
        """CREATE TABLE IF NOT EXISTS Productos 
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        categoria TEST NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL
        )"""
    )

    # realizar un commit (guardar los cambios) si se actualizo algo
    conexion.commit

    # cerrar la conexion
    conexion.close()


def insertarProductoEnTabla(producto):

    # conectarse a la base de datos
    conexion = sqlite3.connect(ruta)
    punteroCursor = conexion.cursor()

    # guardar en el puntero los datos del producto
    punteroCursor.execute(
        "INSERT INTO Productos (nombre, descripcion, categoria, cantidad, precio ) VALUES (?, ?, ?, ?, ?)",
        (
            producto["nombre"],
            producto["descripcion"],
            producto["categoria"],
            producto["cantidad"],
            producto["precio"],
        ),
    )

    # guardar cambios y cerrar la conexion
    conexion.commit()
    conexion.close()


def obtenerProductosDeLaTabla():

    # se conecta a la base de datos
    conexion = sqlite3.connect(ruta)
    punteroCursor = conexion.cursor()

    # se obtine la direccion de memoria donde se encuentra la tabla
    punteroCursor.execute("SELECT * FROM Productos")

    # guarda en una lista los datos de la tabla
    listaProductos = punteroCursor.fetchall()

    # cierra la conexion
    conexion.close()

    # retorna el valor de la lista
    return listaProductos


def actualizarProductoDeLaTabla(id, cantNueva):

    # conectarse a la base de datos
    conexion = sqlite3.connect(ruta)
    punteroCursor = conexion.cursor()

    # guardar en el puntero los datos del producto
    punteroCursor.execute(
        "UPDATE Productos SET cantidad = ? WHERE id = ?", (cantNueva, id)
    )

    # guardar cambios y cerrar la conexion
    conexion.commit()
    conexion.close()


def eliminarProductoDeLatabla(id):

    # conectarse a la base de datos
    conexion = sqlite3.connect(ruta)
    punteroCursor = conexion.cursor()

    # guardar en el puntero los datos del producto
    punteroCursor.execute("DELETE FROM Productos WHERE id = ?", (id,))

    # guardar cambios y cerrar la conexion
    conexion.commit()
    conexion.close()


def buscarProductoDeLaTabla(id):

    # conectarse a la base de datos
    conexion = sqlite3.connect(ruta)
    punteroCursor = conexion.cursor()

    # guardar en el puntero los datos del producto
    punteroCursor.execute("SELECT * FROM Productos WHERE id = ?", (id,))

    # guardar en una lista los datos del producto
    listaProducto = punteroCursor.fetchone()

    # cierra la conexion
    conexion.close()

    # retorna el valor de la lista
    return listaProducto


def repotarBajoStockDeLaTabla(condicion):

    # conectarse a la base de datos
    conexion = sqlite3.connect(ruta)
    punteroCursor = conexion.cursor()

    # guardar en el puntero los datos de los productos con menor estock que la condicion
    punteroCursor.execute("SELECT * FROM Productos WHERE cantidad <=?", (condicion,))

    # guardar en una lista los datos del producto
    listaProducto = punteroCursor.fetchall()

    # cierra la conexion
    conexion.close()

    # retorna el valor de la lista
    return listaProducto

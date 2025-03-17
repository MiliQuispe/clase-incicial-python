import sqlite3  # importar el modulo de sqlLites

# Conectarse o crear la base de datos
conexion = sqlite3.connect(
    r"C:\Users\Milagros quispe\Documents\clases\clase13\inventario.db"
)

# crear un puntero o cursor a la base de datos (funciona como un  puntero a file en archivos en c?)
punteroCursor = conexion.cursor()

# ejecutar una consulta
punteroCursor.execute("SELECT * FROM productos")

# guardos los datos que ejecute en una variable
resultado = punteroCursor.fetchall()
print(resultado)

# realizar un commit (guardar los cambios) si se actualizo algo
conexion.commit

# cerrar la conexion
conexion.close()

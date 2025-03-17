""""
import os

def clear_terminal();
    #para windows
    if os.name == "nt":
        os.system("cls")

    #para macOs
    else
"""

# lista => []
# diccionario => {} clave : valor

"""
# 0:nombre, 1:cantidad, 2:precio
producto = ["frutilla", 34, 560.2]
"""
producto_disccionario = {"nombre": "manzana", "cantidad": 54}
print(f"diccionario producto: {producto_disccionario}")
"""
# acceder a los valores[]
print(producto_disccionario["nombre"])  # [clave]
print(producto_disccionario["cantidad"])
# print(producto_disccionario["precio"])
"""
"""
# accerder con get
print(producto_disccionario.get("nombre"))
print(producto_disccionario.get("cantidad"))
# print(producto_disccionario.get("precio"))
"""
"""
# actualizar
print(producto_disccionario.get("cantidad"))
producto_disccionario["cantidad"] = 40
print(producto_disccionario.get("cantidad"))
"""
"""
# updat
producto_disccionario.update({"cantidad": 70})
print(producto_disccionario.get("cantidad"))
"""

"""
# agregar
print(producto_disccionario)
producto_disccionario["precio"] = 1006.50
print(producto_disccionario)
"""


# eliminar
# con pop() como en lista

# for clave in producto_disccionario:
# print(f"clave: {clave}: {producto_disccionario[clave]}")

# solo clave del diccionario
for clave in producto_disccionario.keys():  # ["nombre,"cantidad"]
    print(clave)

# solo los valores de las claves de los diccionario
for values in producto_disccionario.values():  # ["manzana", "54"]
    print(values)


# Los valores de las claves de los diccionario y las claves
for (
    clave,
    values,
) in producto_disccionario.items():  # ["nombre,"manzana"]["cantidad, "54"]
    print(f"clave: {clave}  values: {values}")

for item in producto_disccionario.items():  # ["nombre,"manzana"]["cantidad, "54"]
    print(item)

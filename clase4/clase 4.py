"""
a = 5
b = 8

c = None  # solo es declaracion, no es un tipod edato

print(f"comparamos a > b, resultado: {a > b}")
print(f"comparamos a < b, resultado: {a < b}")
print(f"comparamos a = b, resultado: {a == b}")
print(f"comparamos a != b, resultado: {a != b}")

# las variables se puede cambiar el tipo al asignar
b = 2
print(f"el valor de b es: {b}")

b = "hola"
print(f"el valor de b es: {b}")
"""

""""
 consigna solicitar un numero por consola
 Indicar opciones
 Infromar resultado
"""
# entrada
numero_1 = int(input("ingrese numero_1 "))
numero_2 = int(input("ingrese numero_2 "))

# proceso
print("selecciona el operador:\n")
print("1_ suma")
print("2_ resta")
print("3_ multiplicacion")
print("4_ division")

opcion = int(input("su eleccion es: "))
print(f"su opcion fue: {opcion} ")

# salida

if opcion == 1:
    suma = numero_1 + numero_2
    print(f"El resultado de la suma es {suma}")
elif opcion == 2:
    resta = numero_1 - numero_2
    print(f"El resultado de la resta es {resta}")
elif opcion == 3:
    multiplicacion = numero_1 * numero_2
    print(f"El resultado de la multiplicacion es {multiplicacion}")
elif opcion == 4:
    division = numero_1 / numero_2
    print(f"El resultado de la division es {division}")
else:
    print("La opcion ingreda es incorrecta")

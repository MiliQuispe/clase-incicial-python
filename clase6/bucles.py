# bucles
"""
while True:
    check = input("ingrese x para sali o cualquier tecla para continuar").lower()
    if check == "x":
        break
"""
"""
contador = 0

while contador < 10:
    print(contador)

    contador += 1
"""


"""
contador = 0
acumulador = 0

while contador < 10:

    valor = float(input("ingresed un valor: "))
    acumulador += valor
    print(f"acumulacion parcial: {acumulador}")
    contador += 1

print(f"Acumulacion total: {acumulador}")
"""

"""
contador = 0
meses = 6
acumuladorIngresos = 0

while contador < meses:
    ingreso = float(input(f"ingrese el ingreso del mes {contador + 1} : "))
    acumuladorIngresos += ingreso
    contador += 1

print(f"\nEl ingreso total: {acumuladorIngresos}")

print(f"En promedio el sueldo es: {acumuladorIngresos/meses} ")

"""
"""
cadena = "Python"
indice = 0

while indice < len(cadena):
    print(f"indice: {indice}, letra: {cadena[indice]}")
    indice += 1
"""

cadena = "Python"
indice = 0

while indice < len(cadena):

    if indice % 2 == 0:
        print(f"indice: {indice}, letra: {cadena[indice]. upper()}")  # mayuscula
    else:
        print(f"indice: {indice}, letra: {cadena[indice]. lower()}")  # minuscula

    indice += 1

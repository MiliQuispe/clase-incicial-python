# funciones declaradas y desrrolladas
"""

def saludar():
    print("holiis")
    resultado = "OK"
    return resultado


# llamado o invocacion
retornado = saludar()

print(f"lo que retorna es : {retornado}")
"""

"""
def mostrarMenu():
    print(
        "\t========MENU=========
        1_Agregar un producto
        2_Mostrar producto
        3_Eliminar producto
        4_Salir"
    )


def sumarNumeros(num1, num2):
    resultadoSuma = num1 + num2
    # print(f"La suma da: {suma}")

    return resultadoSuma


def multiplicacionYdivisionDeEnteros(num1, num2):
    multiplicacion = num1 * num2
    division = num1 / num2
    return (multiplicacion, division)  # retorna una tupla
    # return {
    #    "multiplicacion": multiplicacion,
    #    "division": division,
    # }  # retorna un diccionario


mostrarMenu()
print(f"La suma da: { sumarNumeros(4, 5) }")

# resultado = multiplicacionYdivisionDeEnteros(2, 8)
# print(resultado)

resultadoMultiplicacion, resultadoDivision = multiplicacionYdivisionDeEnteros(3, 6)
print(
    f"La Multiplicacion da: {resultadoMultiplicacion}, La division da: {resultadoDivision}"
)
"""

# variables globales
numero = 4
lista = [1, 2]


def incrementar():
    global numero  # primero se indica que es global
    numero += 1
    lista[0] += 1
    lista[1] += 1


print(numero)
print(lista)
incrementar()
print(numero)
print(lista)

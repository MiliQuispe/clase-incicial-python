# declaracion de variables
# inventario=[]

# declaracion de variables


def oopcionUno():
    print("hola")


opcion = input("ingrese un numero: ")
while True:

    if opcion == "1":
        oopcionUno()
        opcion = input("ingrese un numero: ")

    else:
        print("fin")
        break

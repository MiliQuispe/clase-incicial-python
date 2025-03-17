consumo = None
distanciaRecorrido = None
costoCombustible = None

while True:
    # entrada

    print("\nIngrese los valores solicitados\n")
    consumo = float(input("ingrese el consumo cada 100 km: "))
    distanciaRecorrido = float(input("ingrese la distancia recorrida: "))
    costoCombustible = float(input("ingrese el costo del combustible "))

    # proceso

    litrosConsumidos = distanciaRecorrido / consumo
    costoTotal = litrosConsumidos * costoCombustible
    # salida

    print(
        f"si usted recorrio {distanciaRecorrido} kms, va a consumir {litrosConsumidos} litros"
    )
    print(f"\nUsted gasto {costoTotal}")

    # opcion= input("para terminar ingrese una x: ").lower()# convierte a minuscula
    # if opcion == "x":
    #    break

    opcion = input("para terminar ingrese una x: ")
    if opcion == "x" or opcion == "X":
        break

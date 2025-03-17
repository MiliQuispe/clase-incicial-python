# delimitador

cadena = 'Mi libro favorito es "el principito"'
print(cadena)

cadena = "this is juan's book"
print(cadena)


# operador
print("-" * 30)  # repite 30 veces el -

# operador +

var1 = 1
var2 = 2
var3 = "3"
var4 = "4"

print(var1 + var2)
print(var3 + var4)
print(var1 + (int)(var4))


# longitud

cadena = "Python"
print(len(cadena))

for i in cadena:
    print(i)

for i in range(len(cadena)):  # me devuele los indioe
    print(i)

for i in range(len(cadena)):  # me devuele los indioe
    print(f"cadena[{i}] = {cadena[i]}")


# subcadena

subcadena = cadena[0:4]  # str[indice_inicio: indice_fin]
print(subcadena)
subcadena = cadena[0:4]
print(subcadena)

subcadena2 = cadena[2:6]
print(subcadena2)
subcadena2 = cadena[2:]
print(subcadena2)

print(cadena[-4])

# si se pasa de rango da error

cadena = "eStudIANDo pYThON"

print(cadena)
print(cadena.lower())  # .metodo
print(cadena.upper())
print(cadena.title())
print(cadena.capitalize())

number = 10.5
print("round(10,5)", round(10, 5))
print("el indice del espacio es: ", cadena.find(" "))  # me duvuelve la posicion del " "
print(cadena[cadena.find(" ") + 1 :])

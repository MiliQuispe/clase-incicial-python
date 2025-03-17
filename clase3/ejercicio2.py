# Calcula el promedio de lo recaudado en 6 meses

# comentar todo de una es  ctrl+} y para descomentar ves lo mismo

mes_1 = 1500
mes_2 = 1660
mes_3 = 7300
mes_4 = 1789
mes_5 = 2309
mes_6 = 4308

promedio = (mes_1 + mes_2 + mes_3 + mes_4 + mes_5 + mes_6) / 6

print("Lo recaudado en promedio fue: " + str(promedio))  # concatenar cadenas
print("Lo recaudado en promedio fue: ", promedio)  # da coma da formato para que imprima
print(f"Lo recaudado en promedio fue: {promedio}")  # usando f-strinf
print(f"Lo recaudado en promedio fue: {promedio:.2f}")  # para indicar dos decimales
print(
    f"Lo recaudado en promedio fue: {round(promedio,3)}"
)  # para indicar dos decimales

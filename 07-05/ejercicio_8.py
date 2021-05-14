"""
8- Se desea saber la temperatura media trimestral de n paises. Para ello se tiene como
dato las temperaturas medias mensuales de dichos paises.
Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias
mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en
memoria.
a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las
mismas.
c - Calcular la temperatura media trimestral de cada país.
c - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
b - Imprimir el nombre del pais con la temperatura media trimestral mayor.
"""
cantidad = int(input("Ingrese cantidad de paises: "))
paises = []
temp1 = []
temp2 = []
temp3 = []
tempmedias = []

for x in range(cantidad):
    pais = input("Inserte país: ")
    paises.append(pais)
    tempe1 = int(input("Inserte temperatura 1: "))
    temp1.append(tempe1)
    tempe2 = int(input("Inserte temperatura 2: "))
    temp2.append(tempe2)
    tempe3 = int(input("Inserte temperatura 3: "))
    temp3.append(tempe3)

for x in range(len(paises)):
    print(f"Para el pais {paises[x]} la temperatura del primer mes es {temp1[x]}°C, del segundo mes es {temp2[x]}°C y del tercer mes es {temp3[x]}°C.\n")

for x in range(len(paises)):
    tempmedia = (temp1[x] + temp2[x] + temp3[x])/3
    tempmedias.append(tempmedia)
    print(f"Para {paises[x]}, la temperatura media trimestral es de {round(tempmedia, 2)}°C.")

maxtempmedia = max(tempmedias)
max_index = tempmedias.index(maxtempmedia)

print(f"El país con la temperatura media trimestral mas alta es {paises[max_index]} con {round(tempmedias[max_index], 2)}°C.")

input("Presione enter para salir.")



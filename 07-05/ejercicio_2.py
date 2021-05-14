"""
2- Se debe crear y cargar una lista donde almacenar n sueldos. Ordenar de menor a mayor
la lista Mostrar ordenada y cuantos sueldos > 25000 hay.
"""

sueldos = []
monto = 1
contador = 0

while monto != 0:
    monto = int(input("Para salir oprima '0' \n Ingrese el sueldo: "))
    sueldos.append(monto)
    if monto > 25000:
        contador += 1

sueldos.sort()

print("\nLa lista de sueldos ordenada es:")


for x in range(len(sueldos)-1):
    print(f"$ {sueldos[x]}")
print(f"Y {contador} sueldos son mayores a $25000")

print("Presione enter para salir.")


"""
2- Se debe crear y cargar una lista donde almacenar n sueldos. Ordenar de menor a mayor
la lista Mostrar ordenada y cuantos sueldos > 25000 hay.
"""

sueldos = []
monto = 1
while monto != 0:
    monto = int(input("Para salir oprima '0' \n Ingrese el sueldo: "))
    sueldos.append(monto)
sueldos = sueldos.sort()
print(sueldos)

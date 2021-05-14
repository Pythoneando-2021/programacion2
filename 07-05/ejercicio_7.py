"""
7- Se tiene que cargar la siguiente información:
· Nombres de n empleados
· Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.
Confeccionar el programa para:
a) Realizar la carga de los nombres de empleados y los tres sueldos por cada
empleado.
b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3
meses para cada empleado.
c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3
meses
d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado
"""
cantidad = int(input("Ingrese cantidad de empleados: "))

empleados = []
sueldos1 = []
sueldos2 = []
sueldos3 = []
sueldosacum = []

for x in range(cantidad):
    empleado = input("Ingrese el nombre del empleado: ")
    empleados.append(empleado)
    sueldo1 = int(input("Ingrese el primer sueldo del empleado: "))
    sueldos1.append(sueldo1)
    sueldo2 = int(input("Ingrese el segundo sueldo del empleado: "))
    sueldos2.append(sueldo2)
    sueldo3 = int(input("Ingrese el tercer sueldo del empleado: "))
    sueldos3.append(sueldo3)

for x in range(cantidad):
    sueldoacum = sueldos1[x] + sueldos2[x] + sueldos3[x]
    sueldosacum.append(sueldoacum)
    print(f"Para el empleado {empleados[x]}, el total pagado en los ultimos 3 meses es de ${sueldosacum[x]}.")


maxsueldoacum = max(sueldosacum)
max_index = sueldosacum.index(maxsueldoacum)

print(f"El empleado con el mayor ingreso en los últimos 3 meses es {empleados[max_index]} con ${sueldosacum[max_index]}.")

input("Presione enter para salir.")



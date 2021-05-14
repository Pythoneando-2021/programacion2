"""
6- En un curso de n alumnos se registraron las notas de sus exámenes y se deben
procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la
condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está
entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.
"""

cantidad = int(input("Ingrese cantidad de alumnos: "))
nombres = []
notas = []
contador = 0

for x in range(cantidad):
    nombre = input("Ingrese nombre del alumno: ")
    nombres.append(nombre)
    nota = int(input("Ingrese la nota del alumno: "))
    notas.append(nota)

for x in range(cantidad):
    print("====================================")
    print(f"Nombre del alumno: {nombres[x]}")
    print(f"Nota del alumno: {notas[x]}")
    if notas[x] >= 8:
        print("Condición del alumno: Muy bueno")
        contador += 1
    elif notas[x] >= 4 and notas[x] <= 7:
        print("Condición del alumno: Bueno")
    elif notas[x] < 4:
        print("Condición del alumno: Insuficiente")

print("\n")
print(f"Hay {contador} alumnos con la condicion Muy Bueno.")

print("Presione enter para salir.")
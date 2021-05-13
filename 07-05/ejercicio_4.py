"""
4- Crear dos lista paralelas y almacenar los nombres de n países y su población. Ordenar
de mayor a menor por cantidad de habitantes la lista e imprimirla.
"""

cantidad = int(input("Ingrese cantidad de paises: "))
x = 0
paises = []
poblaciones = []

for x in range(cantidad):
    pais = input("Ingrese país: ")
    paises.append(pais)
    poblacion = input("Ingrese población del país: ")
    poblaciones.append(poblacion)

cantidad = cantidad - 1

for k in range(cantidad):
    for x in range(cantidad-k):
        if poblaciones[x] < poblaciones[x+1]:
            aux1 = poblaciones[x]
            poblaciones[x] = poblaciones[x+1]
            poblaciones[x+1] = aux1
            aux2 = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = aux2

print("Lista de paises y sus poblaciones, ordenados de mayor a menor según población:")

for x in range(cantidad+1):
    print(paises[x],poblaciones[x])


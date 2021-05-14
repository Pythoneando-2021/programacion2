"""
5- Crear y cargar dos listas con los nombres de n productos en una y sus respectivos
precios en otra. Definir dos listas paralelas. Mostrar cuantos productos tienen un precio
mayor al primer producto ingresado.
"""
cantidad = int(input("Ingrese cantidad de productos: "))
productos = []
precios = []
productosaux = []
preciosaux = []
contador = 0

for x in range(cantidad):
    producto = input("Ingrese producto: ")
    productos.append(producto)
    precio = int(input("Ingrese el precio del producto:"))
    precios.append(precio)

for x in range(cantidad):
    if precios[x] > precios[0]:
        preciosaux.append(precios[x])
        productosaux.append(productos[x])
    else:
        continue

print("Los productos con mayor precio al primero ingresado son:")

str(preciosaux)

for x in range(len(preciosaux)):
    print(productosaux[x], " $", preciosaux[x])



input("Presione enter para salir")

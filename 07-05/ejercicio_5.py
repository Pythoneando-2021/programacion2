"""
5- Crear y cargar dos listas con los nombres de n productos en una y sus respectivos
precios en otra. Definir dos listas paralelas. Mostrar cuantos productos tienen un precio
mayor al primer producto ingresado.
"""
cantidad = int(input("Ingrese cantidad de productos: "))
productos = []
precios = []
productosaux = []
preciosaux =[]
contador = 0

for x in range(cantidad):
    producto = input("Ingrese producto: ")
    productos.append(producto)
    precio = int(input("Ingrese el precio del producto:"))
    precios.append(precio)

for k in precios:
    if k > precios[0]:
        productosaux.append(productos[contador])
        preciosaux.append(precio[contador])
        contador +=1
    else:
        contador += 1
        continue

print("Los productos con mayor precio al primero ingresado son: ")

for x in range(cantidad):
    print(productosaux[x],preciosaux[x])


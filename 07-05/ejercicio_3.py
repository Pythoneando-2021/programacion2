"""
3- Crear una lista y almacenar los nombres de n ciudades por teclado. Luego permitir
ingresar el nombre de una ciudad y mostrar en qué posición de la lista se encuentra en
caso de no encontrarse mostrar un mensaje.
"""
cantidad = int(input("Ingrese cantidad de ciudades a ingresar: "))
ciudades = []
x = 0

while x < cantidad:
    ciudad = input("Ingrese ciudad: ").lower()
    ciudades.append(ciudad)
    x += 1

x = 0

ciudad2 = input("Ingrese nombre de ciudad a buscar: ").lower()

if ciudad2 in ciudades:
    for c in ciudades:
        if ciudad2 == c:
            print(f"\nLa ciudad {ciudad2.capitalize()} se encuentra en la posición {x+1} de la lista (en el index {x}).")
            break
        else:
            x += 1
else:
    print("\n No se encontró la ciudad")



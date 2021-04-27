"""5- Solicitar la carga del nombre de n personas en mayúscula.
Mostrar un mensaje si comienza con vocal dicho nombre.
"""

vocales = "aeiou"
personasTotales = int(input("Ingrese el total de personas: "))
for i in range(personasTotales):
    nombre = input("Ingrese el nombre de la persona en mayuscula: ")
    if nombre[0].isupper():
        if nombre[0].lower() in vocales:
            print("El nombre comienza con vocal")
    else:
        print("El nombre de la persona debe estar en minusculas")
        break
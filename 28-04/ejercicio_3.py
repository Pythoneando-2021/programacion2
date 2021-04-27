"""3- Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas.
Contar la cantidad de vocales.
"""

vocales = "aeiou"
oracion = input("Ingrese una oracion: ")
def contarVocales(palabra):
    final = [letra for letra in palabra if letra in vocales]
    print("Cantidad de vocales: ", len(final))

contarVocales(oracion)
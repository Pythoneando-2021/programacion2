"""2- Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron.
Tener en cuenta que un espacio en blanco es igual a " ", en cambio una cadena vacía es ""
"""

oracion = input("Ingrese una oracion: ")
espacios = [letra for letra in oracion if letra == " " ]
print("Total de espacios: ", len(espacios))
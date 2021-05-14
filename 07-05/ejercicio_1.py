"""
1- Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la
carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.
"""

valoresEnteros = []
valor = 1
while valor != 0:
    valor = int(input("Para terminar oprima '0' \n Ingrese un valor entero: "))
    valoresEnteros.append(valor)
print("La lista tiene un tamaño de " , len(valoresEnteros) - 1 ," elementos")

print("Presione enter para salir")
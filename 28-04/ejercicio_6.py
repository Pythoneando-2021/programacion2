"""6- Realizar un programa que lea los lados de n triángulos, e informar: a) De cada uno de ellos, qué tipo de triángulo es:
equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual) b) Cantidad de triángulos de cada tipo.
"""

cantidad = int(input("Ingrese la cantidad de triangulos: "))

iso=0
esc=0
equi=0
c=0

while c < cantidad:
    c += 1
    lado1 = int(input("Ingrese el lado 1: "))
    lado2 = int(input("Ingrese el lado 2: "))
    lado3 = int(input("Ingrese el lado 3: "))

    if lado1 == lado2 and lado2 == lado3:
        equi += 1
        print("El triangulo ingresado es equilatero")
    else:
        if lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
            esc += 1
            print("El triangulo ingresado es escaleno")
        else:
            iso += 1
            print("El triangulo ingresado es isoseles")

print ("Hay ",iso," triangulos isoseles, ",esc," triangulos escalenos y ",equi," triangulos equilaterios")
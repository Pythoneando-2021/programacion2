#1- Ingresar un mail y comprobar si tiene el carácter @. Sino lo tiene informar el error.

emailReceived = input("Ingrese su email: ")

for i in emailReceived:
    if i == "@":
        caracter = "Email correcto"
        break
    else:
        caracter = "Ingrese un email valido"
print(caracter)
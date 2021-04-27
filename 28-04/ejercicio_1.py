#1- Ingresar un mail y comprobar si tiene el carácter @. Sino lo tiene informar el error.

emailReceived = input("Ingrese su email: ")


def validateEmail(email):
    checkEmail = email.find("@")
    if checkEmail < 0:
        print("Por favor ingrese un email correcto")
    else:
        print("Email correcto")


validateEmail(emailReceived)


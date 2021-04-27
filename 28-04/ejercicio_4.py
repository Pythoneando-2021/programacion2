"""4- Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres.
Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido,
en caso contrario mostrar un mensaje de error.
"""

def ingresarPassword():
    password = input("Ingrese su clave: ")
    passwordLength = len(password)
    if passwordLength < 10 or passwordLength > 20:
        print("Su password debe tener una longitud entre 10 y 20 caracteres")
        ingresarPassword()
    else:
        print("Password guardada con exito")
ingresarPassword()
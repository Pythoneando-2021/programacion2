"""7- Crear un módulo que solicite al usuario el ingreso de un nombre de usuario y contraseña criterios de aceptación:
    • El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
    • La contraseña debe contener un mínimo de 8 caracteres.
    • La contraseña no puede contener espacios en blanco.
"""

usuario = input("Ingrese el usuario: ")

while len(usuario)<6 or len(usuario)>12:
    usuario = input("Usuario incorrecto, ingrese nuevamente: ")
print("Usuario ingresado")

validacion = True
contra = input("Ingrese la contraseña: ")

while len(contra)<8:
    contra = input("Contraseña demasiado corta, ingrese nuevamente: ")
for x in contra:
    if(x == ' '):
        validacion = False

if validacion:
    print("Contraseña ingresada")
else:
    print("Contraseña no valida, no se permiten espacios")
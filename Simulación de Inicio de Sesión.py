# Simulación de Inicio de Sesión

print("Para iniciar sesion en este correo se rrequiere la clave de acceso")

clave_correcta = "estanoesmicontraseña123"

limite_de_intentos = 3
intentos =  0
acceso_concedido = False

while intentos < limite_de_intentos:

    print(f"intentos{intentos + 1}/{limite_de_intentos}")
    clave = (input("ingrese la contraseña: "))

    if clave == clave_correcta:
        acceso_concedido = True
        break

    else:

        print("Clave incorrecta \n")
        intentos += 1

if acceso_concedido:

    print("Clave correcta. acceso al correo concedido. \n")

else:
    
    print("Se te han acabado los intentos, el correo se a bloqueado por seguridad. \n")
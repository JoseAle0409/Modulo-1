#(examen)El Cajero Automático de Billetes Óptimos

print("\n ----CAJERO DEL BANCO DE VENEZUELA---- \n")

saldo_disponible = 50000
pin_correcto = "5420"
limite_de_intentos = 3
intentos =  0
acceso_concedido = False

while intentos < limite_de_intentos:

    print(f"intentos{intentos + 1}/{limite_de_intentos}")
    pin = (input("ingrese el PIN: "))

    if pin == pin_correcto:
        acceso_concedido = True
        break

    else:

        print("PIN incorrecta \n")
        intentos += 1
    
else:
    
    print("\n Se te han acabado los intentos. Tarjeta bloqueada. \n")

while acceso_concedido:

    print(f"saldo disponible: {saldo_disponible} \n")
    opciones = input("precione 1 para retirar\nprecione 2 para salir\n: ")

    if opciones == "1":
        cantidad = int(input("ingrese el monto a retirar: "))

        if cantidad > saldo_disponible:

            print("\n saldo insuficiente. Podria intentar de nuevo ")
            print("\n" + "="*50)

        elif cantidad % 10 != 0:

            print("\n el monto debe ser un multiplo de 10. Podria intentar de nuevo \n")
            print("\n" + "="*50)
        
        elif cantidad< 0:

            print("\n monto invalido. Podria intentar de nuevo \n")
            print("\n" + "="*50)

        else:

            saldo_disponible -= cantidad
            reserva_cantidad = cantidad

            bs100 = 0
            bs50 = 0
            bs20 = 0
            bs10 = 0
        
            while reserva_cantidad >= 100:

                reserva_cantidad -= 100
                bs100 += 1
                
            while reserva_cantidad >= 50:

                reserva_cantidad -= 50
                bs50 += 1

            while reserva_cantidad >= 20:

                reserva_cantidad -= 20
                bs20 += 1

            while reserva_cantidad >= 10:

                reserva_cantidad -= 10
                bs10 += 1

            print("\n Retiro exitoso: ")

            if bs100 >0: print(f" {bs100} billetes de 100bs")

            if bs50 >0:  print(f" {bs50} billetes de 50bs")

            if bs20 >0:  print(f" {bs20} billetes de 20bs")

            if bs10 >0:  print(f" {bs10} billetes de 10bs")

            print(f"Nuevo saldo dispobible: ${saldo_disponible}\n")
            print("\n" + "="*50)

    elif opciones == "2":

        print("\n Gracias por preferirnos. Regrese cuando nesesite retirar dinero.\n")
        acceso_concedido = False
        
    else:
        print("\n Opción invalida. \n")
        print("\n" + "="*50)






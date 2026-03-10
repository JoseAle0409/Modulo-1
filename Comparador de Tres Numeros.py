#Comparador de Tres Numeros

numero1 = int(input("indique un numero: "))
numero2 = int(input("indique un numero distinto: "))
numero3 = int(input("indique otro numero distinto: "))

if numero1>numero2 and numero1>numero3:

    print(f"el numero mayor es: {numero1}")

elif numero2>numero1 and numero2>numero3:

    print(f"el numero mayor es: {numero2}")

elif numero3>numero1 and numero3>numero2:

    print(f"el numero mayor es: {numero3}")

else:

    print("\n Alparecer a habido un error")
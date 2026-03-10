#Verificador de Paridad

numero1 = int(input("inserte el primer numero: "))
numero2 = int(input("inserte el segundo numero: "))

if numero1%2==0 and numero2%2==0:

    print("ambos numeros son pares!")

elif numero1%2==0 and numero2%2!=0:

    print("solo el primer numero es par")

elif numero1%2!=0 and numero2%2==0:

    print("solo el segundo numero es par")

else:
    print("ninguno de los numeros son pares")
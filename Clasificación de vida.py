#Clasificación de vida

edad = int(input("cuantos años tienes?: "))

if edad<12:

    print("aun eres solo un niño")

elif edad>=12 and edad<18:

    print("ya eres un adolocente")

elif edad>=19 and edad<30:

    print("felicidades eres un adulto joven")

elif edad>=31 and edad<=59:

    print("eres un adulto mayor")

elif edad>=60 and edad<100:

    print("ya se te podria considerar un aciano")

else:

    print("a habido un error, el numero no es valido")
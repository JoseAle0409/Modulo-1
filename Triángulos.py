#Triángulos

lado_A = int(input("\nlado A: "))
lado_B = int(input("\nlado B: "))
lado_C = int(input("\nlado C: "))

if lado_A + lado_B <= lado_C or lado_A + lado_C <= lado_B or lado_B + lado_C <= lado_A:

    print("\nel triangulo no es valido")

elif lado_A == lado_B == lado_C:

    print("\nequilatero")

elif lado_A == lado_B or lado_A == lado_C or lado_B == lado_C:
        
    print("\nisoceles")

else:
    print("\nescaleno")
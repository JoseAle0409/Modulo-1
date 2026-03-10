#Notas Americanas

nota_numero = int(input("\nintroducir nota: "))

if nota_numero >= 90:

    print("\nhaz sacado una A. felicidades\n")

elif nota_numero >= 80 and nota_numero <= 89:

    print("\nhaz sacado una B. no esta nada mal\n")

elif nota_numero >= 70 and nota_numero <= 79:

    print("\nhaz sacado una C. Es aceptable\n")

elif nota_numero >= 60 and nota_numero <= 69:

    print("\nhaz sacado una D. vas mal, deberias esforzarte mas\n")

elif nota_numero >= 0 and nota_numero <= 59:

    print("\nhaz reprobado. tendras que repetir \n")

else:

    print("\nnumero invalido \n")
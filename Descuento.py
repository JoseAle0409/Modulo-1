#Descuento

gasto = float(input("introducir el gasto aqui: "))

descuento = gasto * 0.15

total_gastado = gasto - descuento

if gasto>=100:

    print(f"haz recivido un descuento del 15%, tu gasto final es de: {total_gastado}")

elif gasto<100:

    print(f"no haz resivido el descuento, solo haz gastado: {gasto}")


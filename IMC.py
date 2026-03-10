#IMC

peso_Kg = 55
altura_m = float(1.65)

IMC = (peso_Kg / altura_m**2)

print(f"tu IMC es de: {IMC:.2f}")

if IMC<26.9 and IMC>18.5:

    print("tienes un peso saludable")
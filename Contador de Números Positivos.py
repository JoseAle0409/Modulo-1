#Contador de Números Positivos

numero = int(input("introducir un numero: "))

contador = 0

while numero>0:
    
    print("este numero es positivo")
    numero = int(input("introducir otro numero: "))

    contador += 1

print(f"\n la cantidad de numeros negativos introducidos es de: {contador} \n")
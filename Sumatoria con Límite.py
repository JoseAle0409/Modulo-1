#Sumatoria con Límite

limite = int(input("introducir el limite de la suma= "))

numero_total = 0
contador = 0

while numero_total < limite:

    contador += 1
    numero_total += contador

    print(f"numero sumado {contador}, numero actual: {numero_total}")

print(f"la suma a topado con el límite. \n")
print(f"resultado de la suma: {numero_total} \n")
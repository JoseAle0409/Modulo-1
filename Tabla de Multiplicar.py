#Tabla de Multiplicar

N = int(input("introducir numero de la tabla: "))

cantidad = [1,2,3,4,5,6,7,8,9,10]

for i in cantidad:

    resultado = N * i

    print(f"{N} X {i}= {resultado}")

    
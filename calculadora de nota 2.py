#calculadora de notas 2

nota1 = float(input("introducir primera nota: ")) 
nota2 = float(input("introducir segunda nota: "))
nota3 = float(input("introducir tercera nota: "))

nota123 = nota1 + nota2 + nota3

promedio = nota123 / 3

if promedio >= 60:

     print(f"haz aprobado, tu nota es de: {promedio:.2f} \n")

elif promedio < 60:
     
     print(f"haz reprobado, tu nota es de: {promedio:.2f} \n")
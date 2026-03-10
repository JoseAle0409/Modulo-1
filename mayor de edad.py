#Mayor de edad

edad = int(input("Ingrese su edad: "))

if edad < 18 and edad >= 0:
    print("Eres menor de edad.")

# Nivel 1  
elif edad >= 18 and edad < 65:
    print("Eres un adulto.")
    
elif edad < 0:
    print("Edad no válida. Por favor, ingrese un número positivo.")
    
elif edad >= 65 and edad < 100:
    print("Eres un adulto mayor.")
    
elif edad >= 100:
    print("Edad no válida. Por favor, ingrese un número menor a 100.")
    
else:
    print("Tienes un error, por favor, corregir.")
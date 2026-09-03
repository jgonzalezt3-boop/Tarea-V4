#Es par o impar

#Entrada
#Número
#Proceso
#Verificar si el número % 2 = 0
#Salida
#Es par o impar

#Bosquejo
#Número = 16
#16 % 2 = 0
#Salida = El número 16 es par

Número = int (input("Ingrese el número: "))
if Número % 2 == 0:
    print(f"El número {Número} es par")
else:
    print(f"El número {Número} es impar")

#___________________________________________________________

num = int(input("Ingresa un número: "))

# Ternario: expresión que devuelve un valor u otro según la condición
resultado = "par" if num % 2 == 0 else "impar"

print(f"{num} es {resultado}")


#_______________________________________________________________

#Es par o impar y si es multiplo 3 y de 5

#Entrada
#Número
#Proceso
#Verificar si el número % 2 = 0
#Verificar si el número % 3 = 0
#Verificar si el número % 5 = 0
#Salida
#Es par o impar y si es multiplo 3 y de 5

#Bosquejo
#Número = 16
#16 % 2 = 0
#16 % 3 = 1
#16 % 5 = 1
#Salida = El número 16 es par

Número = int(input("Ingrese el número: "))
if Número % 2 == 0:
    print(f"El número {Número} es par")
else:
    print(f"El número {Número} es impar")

if Número % 3 == 0 and Número % 5 == 0:
    print(f"El número {Número} es múltiplo de 3 y de 5")
elif Número % 3 == 0:
    print(f"El número {Número} es múltiplo de 3")
elif Número % 5 == 0:
    print(f"El número {Número} es múltiplo de 5")
else:
    print(f"El número {Número} no es múltiplo de 3 ni de 5")
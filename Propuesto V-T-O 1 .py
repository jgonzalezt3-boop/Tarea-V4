#Suma dígitos de un número de 3 cifras

#Entrada
#Número de 3 cifras
#Proceso
#Separar las cifras con // y %
#Suma = Cifra1 + Cifra2 + Cifra3
#Salida
#Suma de las cifras

#Bosquejo
#Número = 372
#Cifra1 = 372 // 100 = 3
#Cifra2 = (372 % 100) // 10 = 7
#Cifra3 = 372 % 10 = 2
#Suma = 3 + 7 + 2 = 12
#Salida = La suma de los tres números es 12

Numero = int(input("Ingrese el número de 3 cifras: "))

Centenas = Numero // 100
Decenas = (Numero % 100) // 10
Unidades = Numero % 10
Suma = Centenas + Decenas + Unidades
print(f"La suma de los tres números es {Suma}")
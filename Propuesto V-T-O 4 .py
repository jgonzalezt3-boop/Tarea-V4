#Redondeo por cifra decimal

#Entrada
#Numero
#Decimales
#Proceso
#NumeroRedondeado = round(Numero, Decimales)
#Salida
#NumeroRedondeado

#Bosquejo
#Numero = 3.14159
#Decimales = 2
#NumeroRedondeado = round(3.14159, 2) = 3.14
#Salida = El número 3.14159 redondeado a 2 cifras decimales es 3.14

Número = float(input("Ingrese el número: "))
Decimales = int(input("Ingrese decimales: "))
Resultado =  round(Número, Decimales)
print (Resultado)
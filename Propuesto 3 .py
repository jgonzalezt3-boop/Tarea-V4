#Intercambiar dos variables

#Entrada
#a
#b
#Proceso
#Cambiar el valor de a por b y el valor de b por a
#Salida
#a y b intercambiados

#Bosquejo
#a = 5
#b = 10
#a,b = b,a
#Salida = a = 10, b = 5

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
a,b = b,a
print (f"a = {a}, b = {b}")
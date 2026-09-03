#Calcular el IVA 15%

#Entrada
#Precio
#Proceso
#IVA = Precio * 0.15
#Total = Precio + IVA
#Salida
#IVA y Total

#Bosquejo
#Precio = 1500
#IVA = 1500 * 0.15 = 225
#Total = 1500 + 225 = 1725
#Salida = El IVA es 225 y el total es 1725

Precio = float(input("Ingrese el precio: "))
IVA = Precio * 0.15
Total = Precio + IVA
print (f"El IVA es ${IVA:.2f} y el total es ${Total:.2f}")

#Calcular el IVA 15% y añadirle un descuento del 10% que se aplique antes del IVA.

#Entrada
#Precio
#Proceso
#DESCUENTO = Precio * 0.10
#IVA = (Precio - DESCUENTO) * 0.15
#Salida = El descuento es, el iva es y el total es.

#Bosquejo
#Precio = 1500
#DESCUENTO = 1500 * 0.10 = 150
#IVA = (1500 - 150) * 0.15 = 202.5
#Total = (1500 - 150) + 202.5 = 1552.5
#Salida = El descuento es 150, el IVA es 202.5 y el total es 1552.5

Precio = float(input("Ingrese el precio: "))
DESCUENTO = Precio * 0.10
IVA = (Precio - DESCUENTO) * 0.15
Total = (Precio - DESCUENTO) + IVA
print (f"El descuento es ${DESCUENTO:.2f}, el IVA es ${IVA:.2f} y el total es ${Total:.2f}")
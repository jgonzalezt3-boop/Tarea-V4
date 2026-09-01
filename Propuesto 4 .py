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
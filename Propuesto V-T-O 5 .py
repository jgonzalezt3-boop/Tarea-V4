#Descuento por cantidad 

#Entrada
#Cantidad
#Proceso
#Precio = 12
#Si compro más de 10 * 0.15
#Si compro entre 5 y 9 * 0.5
#Si compro menos de 5 no hay descuento
#Salida
#Precio unitario
#Descuento
#Total

#Bosquejo
#Cantidad = 12
#Proceso
#Precio = 12
#Si compro más de 10 * 0.15 = 1.8
#Salida
#Precio unitario = 12
#Descuento = 1.8
#Total = 12 - 1.8 = 10.2

Cantidad = int(input("Ingrese la cantidad de productos: "))
PRECIO = 12

if Cantidad >= 10:
    descuento = PRECIO * 0.15
elif Cantidad >= 5:
    descuento = PRECIO * 0.05
else:
    descuento = 0

Total = PRECIO - descuento
print(f"Precio unitario: {PRECIO}")
print(f"Descuento: {descuento:.2f}")
print(f"Total: {Total:.2f}")


PRECIO = 12
cant = int(input("Cantidad: "))

# Determinar el descuento
if cant >= 10:
    descuento = 0.15
elif cant >= 5:
    descuento = 0.05
else:
    descuento = 0

subtotal = PRECIO * cant
total = subtotal * (1 - descuento)

print(f"Precio unitario: ${PRECIO}")
print(f"Descuento: {int(descuento*100)}%")
print(f"Total: ${total:.2f}")
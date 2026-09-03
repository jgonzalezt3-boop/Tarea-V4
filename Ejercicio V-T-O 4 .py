#Cambio de billetes

#Entrada
#Monto
#Proceso
#Dividir sucesivamente por 20, 10, 5, 1 con // y %
#Salida
#Cantidad de billetes de cada tipo

#Bosquejo
#Monto = 87
#Billetes de 20 = 87 // 20 = 4, sobra 7
#Billetes de 10 = 7 // 10 = 0, sobra 7
#Billetes de 5 = 7 // 5 = 1, sobra 2
#Billetes de 1 = 2 // 1 = 2, sobra 0

Monto = int(input("Monto: $ "))
Resto = Monto

Billete_20 = Resto // 20; Resto = Resto % 20
Billete_10 = Resto // 10; Resto = Resto % 10
Billete_5  = Resto // 5;  Resto = Resto % 5
Billete_1  = Resto // 1;  Resto = Resto % 1

print(f"Billetes de $20: {Billete_20}")
print(f"Billetes de $10: {Billete_10}")
print(f"Billetes de $5:  {Billete_5}")
print(f"Billetes de $1:  {Billete_1}")

#__________________________________________________________

#Cambio de billetes agregrando el de 50

#Entrada
#Monto
#Proceso
#Dividir sucesivamente por 50, 20, 10, 5, 1 con // y %
#Salida
#Cantidad de billetes de cada tipo

#Bosquejo
#Monto = 87
#Billetes de 50 = 87 // 50 = 1, sobra 37
#Billetes de 20 = 37 // 20 = 1, sobra 17
#Billetes de 10 = 17 // 10 = 1, sobra 7
#Billetes de 5 = 7 // 5 = 1, sobra 2
#Billetes de 1 = 2 // 1 = 2, sobra 0

Monto = int(input("Monto: $ "))
Resto = Monto

Billete_50 = Resto // 50; Resto = Resto % 50
Billete_20 = Resto // 20; Resto = Resto % 20
Billete_10 = Resto // 10; Resto = Resto % 10
Billete_5  = Resto // 5;  Resto = Resto % 5
Billete_1  = Resto // 1;  Resto = Resto % 1

print(f"Billetes de $50: {Billete_50}")
print(f"Billetes de $20: {Billete_20}")
print(f"Billetes de $10: {Billete_10}")
print(f"Billetes de $5:  {Billete_5}")
print(f"Billetes de $1:  {Billete_1}")

#______________________________________________________________________

#Cambio de billetes y monedas

#Entrada
#Monto
#Proceso
#Convertir el monto a centavos
#Dividir sucesivamente por 5000, 2000, 1000, 500, 100,
#25, 10, 5 y 1 usando // y %
#Salida
#Cantidad de billetes y monedas de cada tipo

#Bosquejo
#Monto = 87.36
#Total de centavos = 87.36 * 100 = 8736
#Billetes de 50 = 8736 // 5000 = 1, sobra 3736
#Billetes de 20 = 3736 // 2000 = 1, sobra 1736
#Billetes de 10 = 1736 // 1000 = 1, sobra 736
#Billetes de 5 = 736 // 500 = 1, sobra 236
#Billetes de 1 = 236 // 100 = 2, sobra 36
#Monedas de 0.25 = 36 // 25 = 1, sobra 11
#Monedas de 0.10 = 11 // 10 = 1, sobra 1
#Monedas de 0.05 = 1 // 5 = 0, sobra 1
#Monedas de 0.01 = 1 // 1 = 1, sobra 0
#Salida = 1 billete de $50, 1 de $20, 1 de $10,
#1 de $5, 2 de $1, 1 moneda de $0.25,
#1 moneda de $0.10 y 1 moneda de $0.01

Monto = float(input("Monto: $ "))

TotalCentavos = int(Monto * 100)

Resto = TotalCentavos

Billete_50 = Resto // 5000; Resto = Resto % 5000

Billete_20 = Resto // 2000; Resto = Resto % 2000

Billete_10 = Resto // 1000; Resto = Resto % 1000

Billete_5 = Resto // 500; Resto = Resto % 500

Billete_1 = Resto // 100; Resto = Resto % 100

Moneda_25 = Resto // 25; Resto = Resto % 25

Moneda_10 = Resto // 10; Resto = Resto % 10

Moneda_5 = Resto // 5; Resto = Resto % 5

Moneda_1 = Resto // 1; Resto = Resto % 1

print(f"Billetes de $50: {Billete_50}")
print(f"Billetes de $20: {Billete_20}")
print(f"Billetes de $10: {Billete_10}")
print(f"Billetes de $5: {Billete_5}")
print(f"Billetes de $1: {Billete_1}")

print(f"Monedas de $0.25: {Moneda_25}")
print(f"Monedas de $0.10: {Moneda_10}")
print(f"Monedas de $0.05: {Moneda_5}")
print(f"Monedas de $0.01: {Moneda_1}")
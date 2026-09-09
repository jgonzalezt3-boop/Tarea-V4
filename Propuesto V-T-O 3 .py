#Índice de masa corporal (IMC)

#Entrada
#Peso en kilogramos
#Altura en metros

#Proceso
#IMC = Peso / (Altura ** 2)

#Salida
#IMC

Peso = float(input("Ingrese el peso en kilogramos: "))
Altura = float(input("Ingrese la altura en metros: "))

IMC = Peso / (Altura ** 2)
print(f"El Índice de Masa Corporal es: {IMC:.2f}")

nombre = input("Ingrese el nombre: ")
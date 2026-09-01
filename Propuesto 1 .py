#Convertir de grados Celcius a Fahrenheit

#Entrada
#Celcius
#Proceso
#Aplicar la formula Fahre = Cels * 9/5 + 32
#Salida 
#Fahrenheit

#Bosquejo
#Cels = 10
#Fahre = 10 * 9/5 + 32 = 50
#Salida = "Los grados Fahrenheit son 50"

Cels = float(input("Ingrese los grados Celsius °C: "))
Fahren = Cels * 9/5 + 32
print (f"Los grados Fahrenheit son : {Fahren:.1f} °F")

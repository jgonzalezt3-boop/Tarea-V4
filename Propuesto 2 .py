#Segundos a horas, minutos y segundos

#Entrada
#TotalDeSegundos
#Proceso
#Horas = TotalDeSegundos // 3600
#Resto = TotalDeSegundos % 3600
#Minutos = Resto // 60
#Segundos = Resto % 60
#Salida
#Horas, minutos y segundos

#Bosquejo
#TotalDeSegundos = 3725
#Horas = 3725 // 3600 = 1
#Resto = 3725 % 3600 = 125
#Minutos = 125 // 60 = 2
#Segundos = 125 % 60 = 5
#Salida = 1 hora, 2 minutos y 5 segundos

TotalDeSegundos = int(input("Ingrese el total de segundos: "))
Horas = TotalDeSegundos // 3600
Resto = TotalDeSegundos % 3600
Minutos = Resto // 60
Segundos = Resto % 60
print (f"{Horas}:{Minutos:02d}:{Segundos:02d}")



total = int(input("Segundos totales: "))
horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60
print(f"{horas}:{minutos:02d}:{segundos:02d}")
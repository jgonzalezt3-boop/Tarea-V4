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
print (f"{Horas:.02f}:{Minutos:02d}:{Segundos:02d}")

#__________________________________________________________

#Segundos a horas, minutos y segundos al reves

#Entrada
#Hora = hh:mm:ss
#Proceso
#Horas, Minutos, Segundos = Hora.split(":")
#Horas = int(Horas)
#Minutos = int(Minutos)
#Segundos = int(Segundos)
#TotalDeSegundos = Horas * 3600 + Minutos * 60 + Segundos
#Salida
#Total de segundos

#Bosquejo
#Hora = 02:30:15
#Horas = 02
#Minutos = 30
#Segundos = 15
#TotalDeSegundos = (2 * 3600) + (30 * 60) + 15
#TotalDeSegundos = 7200 + 1800 + 15
#TotalDeSegundos = 9015
#Salida = 9015 segundos

Hora = input("Ingrese la hora (hh:mm:ss): ")

Horas, Minutos, Segundos = Hora.split(":")  #corta el texto cada vez que encuentra : y guarda las partes en las variables Horas, Minutos y Segundos

Horas = int(Horas)
Minutos = int(Minutos)
Segundos = int(Segundos)

TotalDeSegundos = Horas * 3600 + Minutos * 60 + Segundos

print(f"Total de segundos: {TotalDeSegundos}")
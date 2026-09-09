#Convertir minutos a horas y minutos

#Entrada
#TotalDeMinutos
#Proceso
#Horas = TotalDeMinutos // 60
#Minutos = TotalDeMinutos % 60
#Salida
#Horas y minutos

#Bosquejo
#TotalDeMinutos = 125
#Horas = 125 // 60 = 2
#Minutos = 125 % 60 = 5
#Salida = 2 horas y 5 minutos

TotalDeMinutos = int(input("Ingrese el total de minutos: "))
Horas = TotalDeMinutos // 60
Minutos = TotalDeMinutos % 60
print (f"{Horas} horas y {Minutos} minutos")
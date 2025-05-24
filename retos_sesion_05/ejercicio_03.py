segundos = 1000000
minutos = segundos / 60

minutos = segundos // 60
segundos_resto = segundos % 60

horas = minutos // 60
minutos_resto = minutos % 60

dias = horas // 24
horas_resto = horas % 24

semanas = dias // 7
dias_resto = dias % 7

print(semanas, dias,horas,minutos,segundos)


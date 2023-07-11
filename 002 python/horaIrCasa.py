import datetime

horaActual = datetime.datetime.now()

soloHoraActual = horaActual.hour
soloMinutoActual= horaActual.minute

if soloHoraActual >= 19:
    print("Es la hora de ir a casa.")
else:
    minutos_restantes = ((19 - soloHoraActual -1) * 60 ) + (60 - soloMinutoActual)

    horas_restantes = minutos_restantes / 60

    print("Aún quedan", horas_restantes, "horas para ir a casa.")

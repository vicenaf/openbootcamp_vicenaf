#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

#wikipedia
#Año bisiesto es el divisible entre 4, salvo que sea año secular -último de cada siglo, terminado en «00»-, en cuyo caso también ha de ser divisible entre 400.
#Un año es bisiesto si es:
# Divisible entre 4.
# No divisible entre 100, excepto si es Divisible entre 400

anoAcomprobar = 2001
#defino una variable a falso que modificare si es bisiesto
esBisiesto = False

#realizo el calculo y si cumple condiciones cambio la variable
if anoAcomprobar % 4 == 0:
    if anoAcomprobar % 100 == 0:
        if anoAcomprobar % 400 == 0:
            esBisiesto = True
    else:
        esBisiesto = True
        
#muestro resultado
if esBisiesto == True:
    print ("el año ", anoAcomprobar, " SI es bisiesto")
else:
    print ("el año ", anoAcomprobar, " NO es bisiesto")




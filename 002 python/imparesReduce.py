# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los 
# elementos impares de una lista pasada por parámetro con filter y realizará una 
# suma de todos estos elementos obtenidos mediante reduce.

from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def es_impar(numero):
    return numero % 2 != 0

impares = list(filter(es_impar, numeros))

def sumar(x, y):
    return x + y

resultado = reduce(sumar, impares)

print("Total:", resultado)


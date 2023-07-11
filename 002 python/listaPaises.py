# Crea un script que le pida al usuario una lista de países (separados por comas). 
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

entrada_usuario = input("Ingrese países separados por comas: ")
lista_paises = entrada_usuario.split(",")
lista_paises = [pais.strip() for pais in lista_paises]
lista_paises = list(set(lista_paises))
lista_paises.sort()
paises_formateados = ", ".join(lista_paises)
print("Lista de países:", paises_formateados)

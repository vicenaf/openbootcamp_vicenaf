
# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# Color
# Ruedas
# Puertas

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# Velocidad
# Cilindrada

# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.


class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada




# Creo un Coche
miCoche = Coche("Rojo", 4, 2, 200, 2000)

# Muestro los atributos del coche
print("Color:", miCoche.color)
print("Ruedas:", miCoche.ruedas)
print("Puertas:", miCoche.puertas)
print("Velocidad:", miCoche.velocidad)
print("Cilindrada:", miCoche.cilindrada)
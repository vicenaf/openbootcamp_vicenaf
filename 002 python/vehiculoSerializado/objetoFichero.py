# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis 
# una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

import pickle

class Vehículo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def getMarca (self):
        return self.marca
    
    def getModelo (self):
        return self.modelo

mi_vehiculo = Vehículo("Seat", "Arosa")

with open("vehiculo.bin", "wb") as archivo:
    pickle.dump(mi_vehiculo, archivo)

with open("vehiculo.bin", "rb") as archivo:
    vehiculo_cargado = pickle.load(archivo)

print(vehiculo_cargado.marca)
print(vehiculo_cargado.modelo)

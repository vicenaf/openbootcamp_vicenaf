# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno
# que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar 
# sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def mostrarMensaje(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)
    
    def mostrarResultado(self):
        if self.nota >= 5:
            print("El alumno", self.nombre, "esta aprobado.")
        else:
            print("El alumno", self.nombre, "esta suspendido.")

# Crear un objeto y mostrar datos y aprobado
alumno001 = Alumno("Juan", 5.01)
alumno001.mostrarMensaje()
alumno001.mostrarResultado()
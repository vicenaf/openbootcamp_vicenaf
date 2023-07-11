
# En este ejercicio tenéis que crear una lista de RadioButton que muestre 
# la opción que se ha seleccionado y que contenga un botón de reinicio para
# que deje todo como al principio.

# Al principio no tiene que haber una opción seleccionada.


import tkinter as tk
from tkinter import ttk

def reiniciarSeleccion():
    seleccion.set(None)

def mostrarSeleccion():
    print("Opción seleccionada:", seleccion.get())

ventana = tk.Tk()
ventana.title("Selección de opción")

seleccion = tk.StringVar()

radioButton1 = ttk.Radiobutton(ventana, text="opcion1", variable=seleccion, value='1')
radioButton1.pack()

radioButton2 = ttk.Radiobutton(ventana, text="opcion2", variable=seleccion, value='2')
radioButton2.pack()

radioButton3 = ttk.Radiobutton(ventana, text="opcion3", variable=seleccion, value='3')
radioButton3.pack()

botonReinicio = ttk.Button(ventana, text="Reiniciar selección", command=reiniciarSeleccion)
botonReinicio.pack()

botonMostrar = ttk.Button(ventana, text="Mostrar selección", command=mostrarSeleccion)
botonMostrar.pack()

ventana.mainloop()

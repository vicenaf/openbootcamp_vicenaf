
# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: 
# la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido
# que también será de tipo texto.

# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.


import sqlite3

conexion = sqlite3.connect('alumnos.db')

cursor = conexion.cursor()

cursor.execute('CREATE TABLE Alumnos (id INTEGER PRIMARY KEY,nombre TEXT, apellido TEXT)')

alumnos = [
    (1, 'Juan', 'Perez'),
    (2, 'Maria', 'Garcia'),
    (3, 'Carlos', 'Lopez'),
    (4, 'Fernando', 'Fernandez'),
    (5, 'Ruben', 'Perez'),
    (6, 'Ana', 'Martinez'),
    (7, 'Pedro', 'Sanchez'),
    (8, 'Sara', 'Gonzalez')
]

cursor.executemany('INSERT INTO Alumnos VALUES (?, ?, ?)', alumnos)

nombreBuscado = 'Pedro'
cursor.execute('SELECT * FROM Alumnos WHERE nombre = ?', (nombreBuscado,))
alumnoEncontrado = cursor.fetchone()

if alumnoEncontrado:
    print("ID:", alumnoEncontrado[0])
    print("Nombre:", alumnoEncontrado[1])
    print("Apellido:", alumnoEncontrado[2])
else:
    print("No se encontro el dato buscado", nombreBuscado)

cursor.close()
conexion.close()


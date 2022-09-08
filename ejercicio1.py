# En este ejercicio tendréis que crear una tabla llamada Alumnos
# que constará de tres columnas: 
# la columna id de tipo entero, 
# la columna nombre que será de tipo texto y
# la columna apellido que también será de tipo texto.

#Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
#Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola

from os import curdir
import sqlite3


def main():
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = "SELECT * FROM alumnos WHERE nombre = 'alfonso'"
    
    rows = cursor.execute(query)
    for row in rows:
        print(row)







if __name__ == '__main__':
    main()

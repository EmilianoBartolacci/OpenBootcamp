# Bartolacci Emiliano
# Ejercicio 11

import sqlite3

# con este codigo podemos insertar o buscar a un alumno en la base de datos

print("Que quieres hacer: ¿INSERTAR o BUSCAR?")
queHacer = input()

if queHacer == "INSERTAR" or queHacer == "insertar":
    def main():
        print("inserta el id del alumno:")
        id = int(input())
        print("inserta el nombre del alumno:")
        nombre = input()
        print("inserta el apellido del alumno:")
        apellido = input()
        crear_usuario(id, nombre, apellido)

    def crear_usuario(id, nombre, apellido):
        conn = sqlite3.connect('Ejercicio11.db')
        cursor = conn.cursor()

        query = f"INSERT INTO Alumnos(id, nombre, apellido) VALUES({id}, '{nombre}', '{apellido}')"
        rows = cursor.execute(query)

        conn.commit()
        cursor.close()
        conn.close()
        print("alumno insertado!")

    if __name__ == '__main__':
        main()

elif queHacer == "BUSCAR":
    print("por que quieres buscar: ¿ID, NOMBRE O APELLIDO?")
    parametro = input()
    conn = sqlite3.connect('Ejercicio11.db')
    cursor = conn.cursor()

    if parametro == "ID" or parametro == "id":
        print("inserta el id del alumno:")
        id = input()
        rows = cursor.execute(f'SELECT * FROM Alumnos WHERE id="{id}"')
        for row in rows:
            print(row)
    elif parametro == "NOMBRE" or parametro == "nombre":
        print("inserta el nombre del alumno:")
        nombre = input()
        rows = cursor.execute(f'SELECT * FROM Alumnos WHERE nombre="{nombre}"')
        for row in rows:
            print(row)
    elif parametro == "APELLIDO" or parametro == "apellido":
        print("inserta el apellido del alumno:")
        apellido = input()
        rows = cursor.execute(f'SELECT * FROM Alumnos WHERE apellido="{apellido}"')
        for row in rows:
            print(row)

    cursor.close()
    conn.close()

# Bartolacci Emiliano
# Ejercicio 6 parte dos

class Alumno:
    nombre = "emiliano"
    nota = 6

    def inicioAtributos(self):
        if self.nota >= 5:
            print("El alumno", Alumno.nombre, "a aprobado con la nota de", Alumno.nota)
        else:
            print("El alumno", Alumno.nombre, "a desaprobado con la nota de", Alumno.nota)

objeto = Alumno()
objeto.inicioAtributos()

# output =
# El alumno emiliano a aprobado con la nota de 6

# Bartolacci Emiliano
# Ejercicio 6 parte uno

class Vehiculo:
    Color = "Rojo"
    Ruedas = 4
    Puertas = 5

class Coche(Vehiculo):
    Velocidad = 180
    Cilindrada = 200

objeto = Coche()
print(objeto.Color)
print(objeto.Ruedas)
print(objeto.Puertas)
print(objeto.Velocidad)
print(objeto.Cilindrada)

# output =
# Rojo
# 4
# 5
# 180
# 200

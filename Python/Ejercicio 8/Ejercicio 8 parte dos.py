# Bartolacci Emiliano
# Ejercicio 8 parte uno

import pickle

class Vehiculo :
    velocidadMaxima = 180
    puertas = 5
    precio = 2058912

    def __init__ (self, velocidadMaxima, puertas, precio):
        self.velocidadMaxima = velocidadMaxima
        self.puertas = puertas
        self.precio = precio

    def getVelocidadMaxima(self):
        return self.velocidadMaxima

# aqui guardamos todos los datos en un fichero binario
#objeto = Vehiculo(200, 6, 4253418)
#f = open('datos.bin', 'wb')
#pickle.dump(objeto, f)
#f.close()

f = open('datos.bin', 'rb')
objeto = pickle.load(f)
f.close()
print(f"la velocidad del auto es de {objeto.getVelocidadMaxima()} km/h, el precio del auto es de {objeto.precio} y tiene {objeto.puertas} puertas")

# output =
# la velocidad del auto es de 200 km/h, el precio del auto es de 4253418 y tiene 6 puertas

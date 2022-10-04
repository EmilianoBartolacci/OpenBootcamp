# Bartolacci Emiliano
# Ejercicio 9 parte dos

from functools import reduce
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def impares(x):
    if x % 2 != 0 :
        return True

    return False

def suma(a, b):
    return a + b

listaFiltrada = list(filter(impares, lista))
listaSuma = reduce(suma, listaFiltrada)

print(listaSuma)

# output =
# 36

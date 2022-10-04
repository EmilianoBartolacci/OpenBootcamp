# Bartolacci Emiliano
# Ejercicio 9 parte uno

def Paises():
    lisaPaises = input()
    separacionListaPaises = lisaPaises.split(", ")
    setListaPaises = list(set(separacionListaPaises))
    setListaPaises.sort()

    print(', '.join(setListaPaises))

Paises()

# input = Argentina, Holanda, Francia, Argentina, Belgica
# output = Argentina, Belgica, Francia, Holanda
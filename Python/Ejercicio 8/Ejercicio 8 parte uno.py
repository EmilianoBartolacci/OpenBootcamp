# Bartolacci Emiliano
# Ejercicio 8 parte uno

def saltoLinea (fichero, datos):
    ficheroOpen = open(fichero, 'a')

    for i in datos :
        if not i.endswith('\n'):
            i = i + '\n'
        ficheroOpen.write(i)

    ficheroOpen.close()

listaFichero = [
    "primera linea de caracteres",
    "segunda linea de caracteres",
    "tercera linea de caracteres"
]

saltoLinea('ficheroTxt.txt', listaFichero)

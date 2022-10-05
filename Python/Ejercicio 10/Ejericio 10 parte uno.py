# Bartolacci Emiliano
# Ejercicio 10 parte uno

import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# esta funcion deselecciona los botones ya pulsados
def effacer():
    seleccionado.set(None)

seleccionado = tkinter.StringVar()
print(seleccionado)
botonUno = ttk.Radiobutton(window, text='botonUno', value='2', variable=seleccionado)
botonDos = ttk.Radiobutton(window, text='botonDos', value='3', variable=seleccionado)
botonTres = ttk.Radiobutton(window, text='botonTres', value='4', variable=seleccionado)
botonCuatro = ttk.Radiobutton(window, text='botonReiniciar', value=None, variable=seleccionado, command=effacer)

botonUno.grid(column = 0, row = 1, pady = 5, padx = 5)
botonDos.grid(column = 0, row = 2, pady = 5, padx = 5)
botonTres.grid(column = 0, row = 3, pady = 5, padx = 5)
botonCuatro.grid(column = 0, row = 4, pady = 5, padx = 5)

window.mainloop()

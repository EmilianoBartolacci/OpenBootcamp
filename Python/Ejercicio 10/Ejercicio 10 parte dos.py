# Bartolacci Emiliano
# Ejercicio 10 parte dos

import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

seleccionado = tkinter.StringVar()
seleccionadoUno = tkinter.StringVar()
seleccionadoDos = tkinter.StringVar()
seleccionadoTres = tkinter.StringVar()

botonUno = ttk.Checkbutton(window, text='Tengo entre 5 y 13 años', variable=seleccionado)
botonDos = ttk.Checkbutton(window, text='Tengo entre 13 y 18 años', variable=seleccionadoUno)
botonTres = ttk.Checkbutton(window, text='Tengo entre 18 y 25 años', variable=seleccionadoDos)
botonCuatro = ttk.Checkbutton(window, text='Tengo mas de 25 años', variable=seleccionadoTres)
label = tkinter.Label(window, text="En que rango de edad te encuentras?", bg="gray", fg="black")

botonUno.grid(row=0, column=0)
botonDos.grid(row=1, column=0)
botonTres.grid(row=2, column=0)
botonCuatro.grid(row=3, column=0)
label.grid(row=4, column=0)

window.mainloop()

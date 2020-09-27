from tkinter import *


def Interfaz():


	ventana=Tk() #Creación
	ventana.title("Organizador de Descargas") #Título
	ventana.geometry("650x200") #Tamaño
	ventana.resizable(False,False) #Modificar tamaño
	ventana.config(bg="gray30") #Color


	milabel = Label(ventana, text="Organizador Descargas")
	milabel.place(x=175, y=50)

	frame=Frame(ventana, relief=("groove"))
	frame.place(x=75, y=100)

	Label(frame, text="Su Carpeta Descargas a sido organizada").pack()






	ventana.mainloop()


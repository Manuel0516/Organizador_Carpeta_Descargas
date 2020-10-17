from tkinter import *


def Interfaz():


	ventana=Tk() #Creación
	ventana.title("Organizador de Descargas") #Título
	ventana.geometry("400x180") #Tamaño
	ventana.resizable(False,False) #Modificar tamaño
	ventana.config(bg="gray30") #Color


	milabel = Label(ventana, text="Organizador Descargas", font=("arial",20,"bold"), fg="black")
	milabel.place(x=50, y=50)

	frame=Frame(ventana, relief=("groove"))
	frame.place(x=30, y=100)

	Label(frame, text="Su Carpeta Descargas a sido organizada", font=("arial",13,"bold"), fg="black").pack()






	ventana.mainloop()


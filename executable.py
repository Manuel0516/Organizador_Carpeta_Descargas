from tkinter import *
import main



#----------------------------------------------------------------------Interfaz-------------------------------------------------------------------------------------

ventana=Tk() #Creación
ventana.title("Organizador de Descargas") #Título
ventana.geometry("650x275") #Tamaño
ventana.resizable(True, True) #Modificar tamaño
ventana.config(bg="gray30") #Color

miFrame=Frame(ventana)
miFrame.pack()

milabel = Label(miFrame, text="Organizador Descargas", font=("arial",20,"bold"), fg="black")
milabel.grid(row=1, column=3)

frame=Frame(miFrame, relief=("groove"))
frame.grid(row=2, column=3)


#------------------------------------------------------------------------Funciones------------------------------------------------------------------------------------
def botonEjecutar():
	Contador = 0
	main.ejecutar(Contador)


	ArchivosMv=Label(miFrame, text=str(Contador) + " Archivos clasificados", font=("arial",15,"bold"), fg="black")
	ArchivosMv.grid(row=6, column=3)
def botonCerrar():

	ventana.destroy()



#-------------------------------------------------------------------------Botones--------------------------------------------------------------------------------------

botonEj=Button(miFrame, text="Organizar", font=("arial", 20, "bold"), fg="black", command=lambda:botonEjecutar()).grid(row=5, column=3)
botonCe=Button(miFrame, text="Cerrar", font=("arial", 20, "bold"), fg="black", command=lambda:botonCerrar()).grid(row=7, column=3)
ventana.mainloop()


from tkinter import *
import os
import glob
import shutil
import Creador_Carpetas
import Organizador
import getpass
import platform
import Comprobador



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


#------------------------------------------------------------------------Variables------------------------------------------------------------------------------------

ruta = ""

sistema = platform.system()


user=getpass.getuser()

tiposCarpetas = ['IMAGENES', 'TEXTO', 'CARPETAS_COMPRIMIDAS', 'CODIGO', 'OTROS', 'VIDEOS', '3D', 'PROGRAMAS']

folders = ['IMAGENES', 'TEXTO', 'CARPETAS_COMPRIMIDAS', 'CODIGO', 'OTROS', 'VIDEOS', '3D', 'PROGRAMAS']

if sistema == "Linux": 
	ruta = '/home/'+ user +'/Descargas'

else:
	print(f"el sistema: {sistema} no es compatible con ese sistema")

#---------------------------------------------------------------------------Funciones------------------------------------------------------------------------------------------------

def botonEjecutar():
	
		
	#-----------------------Creador de Carpetas-------------------------------------------------------------------------------------------------------
	
	Creador_Carpetas.Creador_Carpetas(ruta, tiposCarpetas)
	try:
		Comprobador.Comprobar(ruta, folders)
	except OSError:
		Comprobador.Comprobar(ruta, folders)

	#-----------------------Organizador----------------------------------------------------------------------------------------------------------------
	try:
		Organizador.Organizar(ruta, folders, tiposCarpetas)
		
	except OSError:
		while True:
			Comprobador.Comprobar(ruta, folders)
		
			try:
				Organizador.Organizar(ruta, folders, tiposCarpetas)
				break
			except:
				Comprobador.Comprobar(ruta, folders)
	

	#------------------------Archivos------------------------------------------------------------------------------------------
	ArchivosMv=Label(miFrame, text=str("Su carpeta descargas a sido organizada"), font=("arial",12,"bold"), fg="black")
	ArchivosMv.grid(row=6, column=3)


def botonCerrar():

	ventana.destroy()



#-------------------------------------------------------------------------Botones--------------------------------------------------------------------------------------

botonEj=Button(miFrame, text="Organizar", font=("arial", 20, "bold"), fg="black", command=lambda:botonEjecutar()).grid(row=5, column=3)
botonCe=Button(miFrame, text="Cerrar", font=("arial", 20, "bold"), fg="black", command=lambda:botonCerrar()).grid(row=7, column=3)
ventana.mainloop()

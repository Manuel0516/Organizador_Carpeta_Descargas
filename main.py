import os
import glob
import shutil
import Creador_Carpetas
import Organizador
import getpass
import platform
import Comprobador

def ejecutar(Contador):
	
	ruta = ""

	sistema = platform.system()


	user=getpass.getuser()

	tiposCarpetas = ['IMAGENES', 'TEXTO', 'CARPETAS_COMPRIMIDAS', 'CODIGO', 'OTROS', 'VIDEOS', '3D', 'PROGRAMAS']

	folders = ['IMAGENES', 'TEXTO', 'CARPETAS_COMPRIMIDAS', 'CODIGO', 'OTROS', 'VIDEOS', '3D', 'PROGRAMAS']


	#------------------------------------------------------sistema operativo-----------------------------------
	if sistema == "Windows":
		ruta='C:\\Users\\{}\\Downloads'.format(user)


	if sistema == "Linux": 
		ruta = '/home/'+ user +'/Descargas'

	else:
		print(f"el sistema: {sistema} no es compatible con ese sistema")




	#---------------------------------------------------creacion de carpetas----------------------------------------------------

	Creador_Carpetas.Creador_Carpetas(ruta, tiposCarpetas)
	try:
		Comprobador.Comprobar(ruta, folders)
	except OSError:
		Comprobador.Comprobar(ruta, folders)

	#----------------------------------------------------clasificado-----------------------------------------------------------
	try:
		Organizador.Organizar(ruta, folders, tiposCarpetas, Contador)

	except OSError:
		while True:
			Comprobador.Comprobar(ruta, folders)
			try:
				Organizador.Organizar(ruta, folders, tiposCarpetas)
				break
			except:
				Comprobador.Comprobar(ruta, folders)

	#-----------------------------------------------------guardado-------------------------------------------------------------

	


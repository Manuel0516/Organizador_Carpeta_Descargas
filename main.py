import os
import glob
import shutil
import Creador_Carpetas
import Organizador
import getpass
import platform
import interfaz_grafica
ruta = ""

sistema = platform.system()

user=getpass.getuser()

tiposCarpetas = ['IMAGENES', 'TEXTO', 'CARPETAS_COMPRIMIDAS', 'CODIGO', 'OTROS', 'VIDEOS']

folders = ['IMAGENES', 'TEXTO', 'CARPETAS_COMPRIMIDAS', 'CODIGO', 'OTROS', 'VIDEOS']


#------------------------------------------------------sistema operativo-----------------------------------

if sistema == "Windows":
	ruta = "C:\Users\{}\Downloads".format(user)
	print(sistema)
if sistema == "Linux": 
	ruta = '/home/'+ user +'/Descargas'
	print(sistema)
else:
	print(f"el sistema: {sistema} no es compatible con ese sistema")




#---------------------------------------------------creacion de carpetas----------------------------------------------------

Creador_Carpetas.Creador_Carpetas(ruta)

#----------------------------------------------------clasificado-----------------------------------------------------------



Organizador.Organizar(ruta, folders) 
#-----------------------------------------------------guardado-------------------------------------------------------------

interfaz_grafica.Interfaz()


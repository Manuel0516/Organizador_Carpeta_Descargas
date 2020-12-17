import os



def Creador_Carpetas(ruta, tiposCarpetas):
	
	os.chdir(ruta)
	ruta_lista = os.listdir()

	for i in range(len(tiposCarpetas)):
		if not (tiposCarpetas[i] in ruta_lista):
			os.mkdir(ruta + '/{}/'.format(tiposCarpetas[i]))

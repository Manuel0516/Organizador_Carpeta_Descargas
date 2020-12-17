import os

def Comprobar(ruta, folders):
	archivos = {}

	lista = os.listdir(ruta + '/IMAGENES')
	archivos["IMAGENESA"]=[]
	for i in range(len(lista)):
		archivos["IMAGENESA"].append(lista[i])


	lista = os.listdir(ruta + '/VIDEOS')
	archivos["VIDEOSA"]=[]
	for i in range(len(lista)):
		archivos["VIDEOSA"].append(lista[i])

	lista = os.listdir(ruta + '/TEXTO')
	archivos["TEXTOA"]=[]
	for i in range(len(lista)):
		archivos["TEXTOA"].append(lista[i])

	lista = os.listdir(ruta + '/CARPETAS_COMPRIMIDAS')
	archivos["CARPETAS_COMPRIMIDASA"]=[]
	for i in range(len(lista)):
		archivos["CARPETAS_COMPRIMIDASA"].append(lista[i])

	lista = os.listdir(ruta + '/CODIGO')
	archivos["CODIGOA"]=[]
	for i in range(len(lista)):
		archivos["CODIGOA"].append(lista[i])

	lista = os.listdir(ruta + '/3D')
	archivos["3DA"]=[]
	for i in range(len(lista)):
		archivos["3DA"].append(lista[i])

	lista = os.listdir(ruta + '/PROGRAMAS')
	archivos["PROGRAMASA"]=[]
	for i in range(len(lista)):
		archivos["PROGRAMASA"].append(lista[i])

	lista = os.listdir(ruta + '/OTROS')
	archivos["OTROSA"]=[]
	for i in range(len(lista)):
		archivos["OTROSA"].append(lista[i])

	lista = os.listdir(ruta)
	for i in range(len(lista)):
			if lista[i] in archivos["IMAGENESA"]:
				os.rename(lista[i], "1" + lista[i])

			if lista[i] in archivos["VIDEOSA"]:
				os.rename(lista[i], "1" + lista[i])

			if lista[i] in archivos["TEXTOA"]:
				os.rename(lista[i], "1" + lista[i])

			if lista[i] in archivos["CARPETAS_COMPRIMIDASA"]:
				os.rename(lista[i], "1" + lista[i])

			if lista[i] in archivos["CODIGOA"]:
				os.rename(lista[i], "1" + lista[i])

			if lista[i] in archivos["3DA"]:
				os.rename(lista[i], "1" + lista[i])

			if lista[i] in archivos["PROGRAMASA"]:
				os.rename(lista[i], "1" + lista[i])

			if lista[i] in archivos["OTROSA"]:
				os.rename(lista[i], "1" + lista[i])

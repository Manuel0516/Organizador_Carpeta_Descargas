import os
import shutil


tiposCarpetas = ['IMAGENES', 'TEXTO', 'CARPETAS_COMPRIMIDAS', 'CODIGO', 'OTROS', 'VIDEOS']

folders = ['IMAGENES', 'TEXTO', 'CARPETAS_COMPRIMIDAS', 'CODIGO', 'OTROS', 'VIDEOS']


finalImagenes = ('.jpeg', '.png', '.jpg', '.raw', '.JPG','.JPEG', '.JPG', '.gif', '.RAW', '.psd', '.BMP' )
finalVideos = ('.mp4', '.flv', '.mkv', '.avi', 'm4v', '.mov', '.mpg', '.mpeg', 'wmv')
finalTexto = ('.doc', '.odt', '.pdf', '.ppt', '.txt', 'exc')
finalCarpetasComprimidas = ('.zip', '.rar', '.7z', 'gz', 'gzip', 'tar', 'tgz')
finalCodigo = ('.py', '.pyw', '.js', '.cs', '.html')

def Organizar(ruta, folders):

    lista = os.listdir(ruta)

    for i in range(len(lista)):

        if not(lista[i] in folders):

            try:

                if lista[i].endswith(finalImagenes):
                    shutil.move(lista[i], ruta + '/IMAGENES')
                    print(f"el archivo: {lista[i]} se ha movido a IMAGENES")
                elif lista[i].endswith(finalVideos):
                    shutil.move(lista[i], ruta + '/VIDEOS')
                    print(f"el archivo: {lista[i]} se ha movido a VIDEOS")
                elif lista[i].endswith(finalTexto):
                    shutil.move(lista[i], ruta + '/TEXTO')
                    print(f"el archivo: {lista[i]} se ha movido a TEXTO")
                elif lista[i].endswith(finalCarpetasComprimidas):
                    shutil.move(lista[i], ruta + '/CARPETAS_COMPRIMIDAS')
                    print(f"el archivo: {lista[i]} se ha movido a CARPETAS_COMPRIMIDAS")
                elif lista[i].endswith(finalCodigo):
                    shutil.move(lista[i], ruta + '/CODIGO')
                    print(f"el archivo: {lista[i]} se ha movido a CODIGO")
                else:
                    shutil.move(lista[i], ruta + '/OTROS')
                    print(f"el archivo: {lista[i]} se ha movido a OTROS")
            except:
                shutil.move(lista[i], ruta)
                print(f"el archivo: {lista[i]} no es compatible con la aplicación")    

	


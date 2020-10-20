import os
import shutil



finalImagenes = ('.jpeg', '.png', '.jpg', '.raw', '.JPG','.JPEG', '.JPG', '.gif', '.RAW', '.psd', '.BMP' )
finalVideos = ('.mp4', '.flv', '.mkv', '.avi', 'm4v', '.mov', '.mpg', '.mpeg', 'wmv')
finalTexto = ('.doc', '.odt', '.pdf', '.ppt', '.txt', 'exc')
finalCarpetasComprimidas = ('.zip', '.rar', '.7z', 'gz', 'gzip', 'tar', 'tgz')
finalCodigo = ('.py', '.pyw', '.js', '.cs', '.html')
final3D = ('.stl', 'gcode', '.OBJ', '.glb', '.SVG')
finalProgramas = ('.exe', '.deb')


def Organizar(ruta, folders, tiposCarpetas, Contador):

    lista = os.listdir(ruta)

    for i in range(len(lista)):

        if not(lista[i] in folders):

            try:

                if lista[i].endswith(finalImagenes):

                    shutil.move(lista[i], ruta + '/IMAGENES')
                    print(f"el archivo: {lista[i]} se ha movido a IMAGENES")
                    Contador = Contador + 1

                elif lista[i].endswith(finalVideos):

                    shutil.move(lista[i], ruta + '/VIDEOS')
                    print(f"el archivo: {lista[i]} se ha movido a VIDEOS")
                    Contador = Contador + 1

                elif lista[i].endswith(finalTexto):
                    shutil.move(lista[i], ruta + '/TEXTO')
                    print(f"el archivo: {lista[i]} se ha movido a TEXTO")
                    Contador = Contador + 1

                elif lista[i].endswith(finalCarpetasComprimidas):
                    shutil.move(lista[i], ruta + '/CARPETAS_COMPRIMIDAS')
                    print(f"el archivo: {lista[i]} se ha movido a CARPETAS_COMPRIMIDAS")
                    Contador = Contador + 1

                elif lista[i].endswith(finalCodigo):
                    shutil.move(lista[i], ruta + '/CODIGO')
                    print(f"el archivo: {lista[i]} se ha movido a CODIGO")
                    Contador = Contador + 1

                elif lista[i].endswith(final3D):
                    shutil.move(lista[i], ruta + '/3D')
                    print(f"el archivo: {lista[i]} se ha movido a 3D")
                    Contador = Contador + 1

                elif lista[i].endswith(finalProgramas):
                    shutil.move(lista[i], ruta + '/PROGRAMAS')
                    print(f"el archivo: {lista[i]} se ha movido a PROGRAMAS")
                    Contador = Contador + 1
                else:
                    shutil.move(lista[i], ruta + '/OTROS')
                    print(f"el archivo: {lista[i]} se ha movido a OTROS")
                    Contador = Contador + 1

            except:
                shutil.move(lista[i], ruta)
                print(f"el archivo: {lista[i]} no es compatible con la aplicación")    

	


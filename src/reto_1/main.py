from os import listdir 
from os.path import expandvars, exists, isfile, join
from re import search

#Forma la ruta a user-dirs.dirs
xdg_user_dirs = expandvars('$HOME') + '/.config/user-dirs.dirs'
#Verifica si existe el fichero user-dirs.dirs
if exists(xdg_user_dirs):
    #Extrae la ruta del directorio de descargas del fichero user-dirs.dirs
    fichero = open(xdg_user_dirs)
    for linea in fichero:
        if 'DOWNLOAD' in linea:
            dir_desc =  expandvars(search('"(.+?)"', linea).group(1))
            break
    fichero.close()
    #Lista los ficheros del directorio de descargas y los imprime 
    list_fich = [f for f in listdir(dir_desc) if isfile(join(dir_desc, f))]
    print ("Directorio: " + dir_desc + "\n")
    print(*list_fich, sep = "\n")
else:
    print("No se encuentra el fichero user-dirs.dirs")

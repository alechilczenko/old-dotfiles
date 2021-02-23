#Set a random wallpaper easy!
import random
import os

def random_image():
    wallpaper_list = os.listdir('/home/intrackeable/Documentos/CLI/rwal/images')
    if not wallpaper_list:
        print('No se encontraron fondos de pantalla en esta carpeta')
        exit()
    else:
        image = random.choice(wallpaper_list)
        return image

def set_wallpaper():
    command = 'feh --bg-scale /home/intrackeable/Documentos/CLI/rwal/images/' + random_image()
    change = os.system(command)
    return change

set_wallpaper()


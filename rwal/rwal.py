#Set a random wallpaper easy!
import random
import os
from colorama import Fore

global red, green
red = Fore.RED

def get_random_image(path):
    wallpaper_list = os.listdir(path)
    if not wallpaper_list:
        print('{}WALLPAPERS NOT FOUND IN THIS FOLDER'.format(red))
        exit()
    else:
        image = path + random.choice(wallpaper_list)
        return image

def get_wallpaper(path):
    wallpaper = get_random_image(path) 
    command = 'feh --bg-fill {}'.format(wallpaper)
    os.system(command)

def main():
    path = '/home/intrackeable/Documentos/CLI/rwal/images/'
    get_wallpaper(path)

if __name__ == '__main__':
    main()


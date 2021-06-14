#!/usr/bin/env python3
#github.com/intrackeable/dotfiles
#Set a random wallpaper and change gaps level

import random
import os
import subprocess

class Ricer:
    def __init__(self, wm_path, wallpaper_path, gaps):
        self.wm_path = wm_path
        self.wallpaper_path = wallpaper_path
        self.gaps = gaps

    def search_images(self):
        files = os.listdir(self.wallpaper_path)
        images = []
        for file in files:
            if file.endswith('png') or file.endswith('jpeg') or file.endswith('jpg'):
                images.append(file)
        if not images:
            subprocess.call('notify-send "No files found in this folder"', shell=True)
            exit()
        else:
            return images

    def random_wallpaper(self):
        wallpaper = self.wallpaper_path + random.choice(self.search_images())
        return wallpaper

    def set_wallpaper(self):
        subprocess.call('feh --bg-fill {}'.format(self.random_wallpaper()), shell=True)
    
    def restart_wm(self):
        subprocess.call('i3-msg restart', shell=True)
    
    def replace_gaps(self):
        if (self.gaps >= 0 and self.gaps <= 30):

            config = open(self.wm_path).read().splitlines()

            for index, element in enumerate(config):
                if element.startswith('gaps inner'):
                    config[index] = 'gaps inner {}'.format(self.gaps)
                if element.startswith('gaps outer'):
                    config[index] = 'gaps outer {}'.format(self.gaps)

            with open(self.wm_path, 'w') as file:
                file.writelines('\n'.join(config))
                
            self.restart_wm()
        else:
            subprocess.call('notify-send "Unexpected level of gaps"', shell=True)
            exit()
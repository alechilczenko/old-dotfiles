#!/usr/bin/env python3
#github.com/intrackeable/dotfiles
#Set a random wallpaper and change gaps level
#New feature: change blur level in picom forks
import random
import os
import subprocess

class Ricer:
    def __init__(self, wm_path, wallpaper_path, blur_path):
        self.wm_path = wm_path
        self.wallpaper_path = wallpaper_path
        self.blur_path = blur_path

    def set_gaps(self, gaps):
        self.gaps = gaps
    
    def set_blur(self, blur):
        self.blur = blur

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
    
    def open_config(self, path):
        return open(path).read().splitlines()
    
    def write_config(self, path, config):
        with open(path, 'w') as file:
            file.writelines('\n'.join(config))
    
    def replace_gaps(self):
        if (self.gaps >= 0 and self.gaps <= 35):

            config = self.open_config(self.wm_path)

            for index, element in enumerate(config):
                if element.startswith('gaps inner'):
                    config[index] = 'gaps inner {}'.format(self.gaps)
                if element.startswith('gaps outer'):
                    config[index] = 'gaps outer {}'.format(self.gaps)

            self.write_config(self.wm_path,config)
            self.restart_wm()
        else:
            subprocess.call('notify-send "Unexpected level of gaps"', shell=True)
            exit()
    
    def replace_blur(self):
        if (self.blur >= 0 and self.blur <= 10):

            config = self.open_config(self.blur_path)

            for index, element in enumerate(config):
                if element.startswith('blur-strength'):
                    config[index] = 'blur-strength = {}'.format(self.blur)

            self.write_config(self.blur_path,config)
        else:
            subprocess.call('notify-send "Incorrect level of blur"', shell=True)
            exit()
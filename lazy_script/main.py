#!/usr/bin/env python3
#https://github.com/intrackeable/dotfiles

from lazy import Ricer
import argparse

def options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-R', help='Set a random wallpaper', dest='wallpaper', action='store_true')
    parser.add_argument('-G', help='Gaps level between [0-30]', type=int, dest='gaps')
    flags = parser.parse_args()
    return flags.wallpaper, flags.gaps

def main():
    wm_path = '/home/intrackeable/.config/i3/config'
    wallpaper_path = '/home/intrackeable/.scripts/rwal/images/'

    wallpaper, gaps = options()

    manager = Ricer(wm_path,wallpaper_path,gaps)

    if gaps and wallpaper:
        manager.set_wallpaper()
        manager.replace_gaps()
    elif gaps:
        manager.replace_gaps()
    elif wallpaper:
        manager.set_wallpaper()

if __name__ == '__main__':
    main()

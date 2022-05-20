# WALLPAPER SCRIPT 

import os
from random import randint

def image(path):
    images_path = path 
    images_names = os.listdir(images_path)
    index = randint(0, len(images_names)-1)
    return images_names[index]

def main():
    # wallpaper directory
    path = "/home/felipe/Imágenes/fondos/"
    img = image(path)
    img_path = path + img 

    # set wallpaper
    os.system(f'feh --bg-fill "{img_path}"') 

main()


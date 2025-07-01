#!/bin/python3

import sys
from PIL import Image
import math
import random

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)

# Truc simple où l'on prend juste 2 couleurs parmi les couleurs du thème Tokyonight
# tokyonight = ['#ff4352', '#ffd750', '#1ba6fa', '#73fbf1', "#2ac3de", "#7dcfff", "#bb9af7", "#c0caf5"]
#
# random.shuffle(tokyonight)
# col1, col2 = tokyonight[:2]


### Truc complexe où l'on extrait les 2 couleurs les plus présentes dans le fond d'écran
img_path, d = sys.argv[1], int(sys.argv[2])
image = Image.open(img_path)
couleurs = image.convert("RGB").getcolors(image.size[0] * image.size[1])

max_occ1, max_col1 = 0, (1000, 1000, 1000)
for couleur in couleurs: #type:ignore
    if couleur[0] > max_occ1:
        max_occ1 = couleur[0]
        max_col1 = couleur[1]

max_occ2, max_col2 = 0, (1000, 1000, 1000)
for couleur in couleurs: #type:ignore
    if couleur[0] > max_occ2 and distance(couleur[1], max_col1) >= d:
        max_occ2 = couleur[0]
        max_col2 = couleur[1]

col1 = ""
for comp in max_col1:
    h = hex(comp)[2:]
    if len(h) == 1:
        col1 += "0"
    col1 += h

col2 = ""
for comp in max_col2:
    h = hex(comp)[2:]
    if len(h) == 1:
        col2 += "0"
    col2 += h

hypr_file = open("/home/caracole/.config/hypr/hyprland.conf")
hypr_conf = hypr_file.readlines()
hypr_file.close()

ligne = hypr_conf.index("# PT DE REPERE, NE PAS CHANGER\n")
orient = random.randint(1, 180)

new_line = f"  col.active_border = rgba({col2}ff) rgba({col1}ff) {orient}deg\n"

hypr_conf[ligne+1] = new_line

hypr_file = open("/home/caracole/.config/hypr/hyprland.conf", "w")
hypr_file.write("".join(hypr_conf))
hypr_file.close()


# waybar_file = open("/home/caracole/.config/waybar/style.css")
# waybar_content = waybar_file.readlines()
# waybar_file.close()
#
# r = random.randint(0, 1)
#
# waybar_content[0] = f"@define-color {["one", "two"][r]} {col1};\n"
# waybar_content[1] = f"@define-color {["one", "two"][1-r]} {col2};\n"
#
# waybar_file = open("/home/caracole/.config/waybar/style.css", "w")
# waybar_file.write("".join(waybar_content))
# waybar_file.close()

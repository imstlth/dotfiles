#!/bin/fish

set dir /home/caracole/Pictures/wallpaper/
set number (cat /home/caracole/Code/nbg)
set n_lines (/bin/ls $dir | wc -l)

swww img -t fade --transition-duration 1.5 "$dir$(/bin/ls $dir | head -n $number | tail -n 1)"

python3 /home/caracole/Code/python/maincolors.py "$dir$(/bin/ls $dir | head -n $number | tail -n 1)" 50

echo "$(math $number % $n_lines + 1)" > /home/caracole/Code/nbg

#!/bin/fish
# Change le fond d'écran tous les jours

swww-daemon &

sleep 0.4

if test $(date +%j) != $(cat /home/caracole/.bg_day)
    /home/caracole/Code/change_bg.fish
    date +%j > /home/caracole/.bg_day
end

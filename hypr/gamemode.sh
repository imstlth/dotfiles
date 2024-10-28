#!/usr/bin/env sh
HYPRGAMEMODE=$(hyprctl getoption animations:enabled | awk 'NR==1{print $2}')
if [ "$HYPRGAMEMODE" = 1 ] ; then
    #alacritty -e sudo -- cpupower frequency-set -g performance en fait vrm pas bon pour le cpu
    notify-send "Game Mode enabled"
    hyprctl --batch "\
        keyword animations:enabled 0;\
        keyword decoration:drop_shadow 0;\
        keyword decoration:blur:enabled 0;\
        keyword general:gaps_in 0;\
        keyword general:gaps_out 0;\
        keyword general:border_size 1;\
        keyword decoration:rounding 0"
    exit
fi
hyprctl reload
#alacritty -e sudo -- cpupower frequency-set -g powersave
notify-send "Game Mode disabled"

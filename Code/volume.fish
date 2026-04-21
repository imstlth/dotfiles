#!/bin/fish

# if test $argv[1] = mute
#     wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle
# else
wpctl set-volume -l 1 @DEFAULT_AUDIO_SINK@ $argv[1]
# end

if string match --regex "fullscreen: 2" $(hyprctl clients)
    set ending $(string shorten --left --char "" --max 4 $(wpctl get-volume @DEFAULT_AUDIO_SINK@))

    # if test $ending = "TED]"
    #     dunstify -t 1200 -a "Volume" "Muet" -I "/usr/share/icons/Papirus/24x24/panel/audio-volume-muted.svg" -h int:value:0 -h string:x-dunst-stack-tag:"volume"
    # else
    set volume $(math "$ending * 100")
    dunstify -t 1200 -a "Volume" "$volume %" -I "/usr/share/icons/Papirus/24x24/panel/audio-volume-high.svg" -h int:value:"$volume" -h string:x-dunst-stack-tag:"volume"
    #end
end

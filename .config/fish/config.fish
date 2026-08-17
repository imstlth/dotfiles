# On lance hyprland maintenant que fish est devenu le shell par défaut :
if status is-login
    if test -z "$DISPLAY" -a "$XDG_VTNR" = 1
        exec start-hyprland > /tmp/hyprland.log
    end
end

# Commands to run in interactive sessions can go here
if status is-interactive
    abbr --add ip ip -c
    abbr --add l lsd -lA
    abbr --add tree ls --tree
    abbr --add rmd rm -rf
    abbr --add mandel QT_QPA_PLATFORM=xcb ~/Downloads/Mandelbulber_v2-2.31-1-x86_64.AppImage

    abbr --add twitch 'chatterino & streamlink --player mpv --twitch-disable-ads --twitch-low-latency twitch.tv/ohnepixel best'
    bind . _puffer_fish_expand_dots
    # Set up fzf key bindings
    fzf --fish | source
    starship init fish | source
end

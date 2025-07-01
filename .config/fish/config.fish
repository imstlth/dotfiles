# On lance hyprland maintenant que fish est devenu le shell par défaut :
if status is-login
    if test -z "$DISPLAY" -a "$XDG_VTNR" = 1
        exec hyprland > /tmp/hyprland.log
    end
end

# Commands to run in interactive sessions can go here
if status is-interactive
    abbr --add ip ip -c
    abbr --add l ls -GlA
    abbr --add tree ls --tree
    abbr --add rmd rm -rf
    abbr --add mandel QT_QPA_PLATFORM=xcb Downloads/Mandelbulber_v2-2.31-1-x86_64.AppImage
    bind . _puffer_fish_expand_dots
    # Set up fzf key bindings
    fzf --fish | source
    starship init fish | source
end


# BEGIN opam configuration
# This is useful if you're using opam as it adds:
#   - the correct directories to the PATH
#   - auto-completion for the opam binary
# This section can be safely removed at any time if needed.
test -r '/home/caracole/.opam/opam-init/init.fish' && source '/home/caracole/.opam/opam-init/init.fish' > /dev/null 2> /dev/null; or true
# END opam configuration

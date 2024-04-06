# Les plugins
# command-not-found n'a pas l'air de fonctionner
plugins=(command-not-found zsh-autosuggestions sudo dirhistory)

bindkey '^K' autosuggest-accept

# Les bindkeys utiles
# Ctrl+L = clear
# Ctrl+_ = undo

# Propre command not found
function command_not_found_handler {
    local purple='\e[1;35m' bright='\e[0;1m' green='\e[1;32m' reset='\e[0m'
    printf 'zsh: command not found: %s\n' "$1"
    local entries=(
        ${(f)"$(/usr/bin/pacman -F --machinereadable -- "/usr/bin/$1")"}
    )
    if (( ${#entries[@]} ))
    then
        printf "${bright}$1${reset} may be found in the following packages:\n"
        local pkg
        for entry in "${entries[@]}"
        do
            # (repo package version file)
            local fields=(
                ${(0)entry}
            )
            if [[ "$pkg" != "${fields[2]}" ]]
            then
                printf "${purple}%s/${bright}%s ${green}%s${reset}\n" "${fields[1]}" "${fields[2]}" "${fields[3]}"
            fi
            printf '    /%s\n' "${fields[4]}"
            pkg="${fields[2]}"
        done
    fi
    return 127
}

# Uncomment the following line to change how often to auto-update (in days).
zstyle ':omz:update' frequency 7

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
# COMPLETION_WAITING_DOTS="true"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
#plugins=(git)

# Commenté parce que ça prend un temps de malade au chargement
#export NVM_DIR="$HOME/.nvm"
#[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
#[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# export FZF_COMPLETION_TRIGGER=';;'
export FZF_DEFAULT_COMMAND="rg --hidden --ignore-case --files"
alias f='vim $(fzf --reverse --multi --cycle --scroll-off 2 --border none --prompt " " --pointer "" --marker "" --preview "bat --pager never --color always --style auto {}" --height 50%)'

# Je kiff trop cette app 
# s-tui
# c'est vrm une dinguerie
alias grep="grep --color=auto"
alias ip="ip -c"

alias ls="colorls --sd -t"
alias l="ls -lA"
alias tree="ls --tree"

alias word="wc -w"
alias lines="wc -l"
alias maxlines="wc -L"

alias clear_hist="echo '' > ~/.zsh_history"
alias clear_python="echo '' > ~/.python_history"
alias update_pip="pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U"

alias rmd="rm -rf"

alias feveryw="sudo find /* 2>/dev/null | grep"
alias dirsize="du -h --max-depth=0"

alias obsidian="obsidian --enable-features=UseOzonePlatform --ozone-platform=wayland"
alias change_bg='truc=/home/caracole/Pictures/wallpaper/; swww img -t any "$truc$(ls $truc | shuf -n 1)"'
#alias mandelbulber_render="cd /home/caracole/mandelbulber/animation/ && cat *.jpg | ffmpeg -framerate 1 -f image2pipe -i - -c:v libx264 -r 30 -pix_fmt yuv420p output.mp4 && mv output.mp4 /home/caracole/Vidéos/"
#alias change_bg="nitrogen --set-zoom-fill --random /home/caracole/Images/wallpaper/"
#alias change_dual="nitrogen --set-zoom-fill --random /home/caracole/Images/dual wallpaper/"
#alias dual_screen="xrandr --auto --output HDMI-1-0 --mode 1920x1080 --right-of eDP-1 && nitrogen --set-zoom-fill --random /home/caracole/Images/dual wallpaper/ && i3-msg restart"
#alias single_screen="xrandr --output HDMI-1-0 --off && nitrogen --set-zoom-fill --random /home/caracole/Images/wallpaper/ && i3-msg restart"
#alias discipline_bg="nitrogen --set-zoom-fill --random /home/caracole/Images/wallpaper/discipline.jpg"

alias c="clear"

#alias get_perf="sudo cpupower info -b"
#alias set_perf="sudo cpupower set -b"
#alias add_ram="sudo swapoff -a && sleep 10 && sudo swapon -a && sudo swapon /swapfile && sudo sysctl -w vm.min_free_kbytes=78993 && sudo sysctl -w vm.swappiness=10"


#alias csdj="pactl load-module module-null-sink sink_name='virtual_speaker' sink_properties=device.description='virtual_speaker' && pactl load-module module-remap-source master='virtual_speaker.monitor' source_name='virtual_mic' source_properties=device.description='virtual_mic'"
#alias close_csdj="pactl unload-module module-null-sink"
# IMPORTANT LES COMMANDES POUR CHANGER TON KERNEL SONT LES SUIVANTES :
# export UUID=$(sudo blkid -s UUID -o value /dev/nvme0n1p2)
# sudo efibootmgr --create --disk /dev/nvme0n1 --part 1 --label "Arch Linux" --loader '\EFI\ArchLinux\vmlinuz-linux' -u "root=UUID=$UUID rw quiet loglevel=3 snd-intel-dspcfg.dsp_driver=3 nvidia_drm.modeset=1 initrd=\\EFI\\ArchLinux\\initramfs-linux.img"

# Pour lancer un script avec la carte Nvidia :
# prime-run glxinfo

setopt autocd
setopt interactivecomments
setopt hist_ignore_space
setopt AUTO_PUSHD
setopt CD_SILENT
setopt APPEND_HISTORY
setopt SHARE_HISTORY
SAVEHIST=10000
HISTSIZE=10000

autoload compinit
compinit

zstyle ':completion::complete:*' gain-privileges 1

# create a zkbd compatible hash;
# to add other keys to this hash, see: man 5 terminfo
typeset -g -A key

key[Home]="${terminfo[khome]}"
key[End]="${terminfo[kend]}"
key[Insert]="${terminfo[kich1]}"
key[Backspace]="${terminfo[kbs]}"
key[Delete]="${terminfo[kdch1]}"
key[Up]="${terminfo[kcuu1]}"
key[Down]="${terminfo[kcud1]}"
key[Left]="${terminfo[kcub1]}"
key[Right]="${terminfo[kcuf1]}"
key[PageUp]="${terminfo[kpp]}"
key[PageDown]="${terminfo[knp]}"
key[Shift-Tab]="${terminfo[kcbt]}"

# setup key accordingly
[[ -n "${key[Home]}"      ]] && bindkey -- "${key[Home]}"       beginning-of-line
[[ -n "${key[End]}"       ]] && bindkey -- "${key[End]}"        end-of-line
[[ -n "${key[Insert]}"    ]] && bindkey -- "${key[Insert]}"     overwrite-mode
[[ -n "${key[Backspace]}" ]] && bindkey -- "${key[Backspace]}"  backward-delete-char
[[ -n "${key[Delete]}"    ]] && bindkey -- "${key[Delete]}"     delete-char
[[ -n "${key[Up]}"        ]] && bindkey -- "${key[Up]}"         up-line-or-history
[[ -n "${key[Down]}"      ]] && bindkey -- "${key[Down]}"       down-line-or-history
[[ -n "${key[Left]}"      ]] && bindkey -- "${key[Left]}"       backward-char
[[ -n "${key[Right]}"     ]] && bindkey -- "${key[Right]}"      forward-char
[[ -n "${key[PageUp]}"    ]] && bindkey -- "${key[PageUp]}"     beginning-of-buffer-or-history
[[ -n "${key[PageDown]}"  ]] && bindkey -- "${key[PageDown]}"   end-of-buffer-or-history
[[ -n "${key[Shift-Tab]}" ]] && bindkey -- "${key[Shift-Tab]}"  reverse-menu-complete

# Finally, make sure the terminal is in application mode, when zle is
# active. Only then are the values from $terminfo valid.
if (( ${+terminfo[smkx]} && ${+terminfo[rmkx]} )); then
	autoload -Uz add-zle-hook-widget
	function zle_application_mode_start { echoti smkx }
	function zle_application_mode_stop { echoti rmkx }
	add-zle-hook-widget -Uz zle-line-init zle_application_mode_start
	add-zle-hook-widget -Uz zle-line-finish zle_application_mode_stop
fi

autoload -Uz up-line-or-beginning-search down-line-or-beginning-search
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search

[[ -n "${key[Up]}"   ]] && bindkey -- "${key[Up]}"   up-line-or-beginning-search
[[ -n "${key[Down]}" ]] && bindkey -- "${key[Down]}" down-line-or-beginning-search

key[Control-Left]="${terminfo[kLFT5]}"
key[Control-Right]="${terminfo[kRIT5]}"

[[ -n "${key[Control-Left]}"  ]] && bindkey -- "${key[Control-Left]}"  backward-word
[[ -n "${key[Control-Right]}" ]] && bindkey -- "${key[Control-Right]}" forward-word


source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern)
ZSH_HIGHLIGHT_STYLES[default]=none
ZSH_HIGHLIGHT_STYLES[unknown-token]=fg=red,bold
ZSH_HIGHLIGHT_STYLES[reserved-word]=fg=cyan,bold
ZSH_HIGHLIGHT_STYLES[suffix-alias]=fg=green,underline
ZSH_HIGHLIGHT_STYLES[global-alias]=fg=magenta
ZSH_HIGHLIGHT_STYLES[precommand]=fg=green,underline
ZSH_HIGHLIGHT_STYLES[commandseparator]=fg=blue,bold
ZSH_HIGHLIGHT_STYLES[autodirectory]=fg=green,underline
ZSH_HIGHLIGHT_STYLES[path]=underline
ZSH_HIGHLIGHT_STYLES[path_pathseparator]=
ZSH_HIGHLIGHT_STYLES[path_prefix_pathseparator]=
ZSH_HIGHLIGHT_STYLES[globbing]=fg=blue,bold
ZSH_HIGHLIGHT_STYLES[history-expansion]=fg=blue,bold
ZSH_HIGHLIGHT_STYLES[command-substitution]=none
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter]=fg=magenta
ZSH_HIGHLIGHT_STYLES[process-substitution]=none
ZSH_HIGHLIGHT_STYLES[process-substitution-delimiter]=fg=magenta
ZSH_HIGHLIGHT_STYLES[single-hyphen-option]=fg=magenta
ZSH_HIGHLIGHT_STYLES[double-hyphen-option]=fg=magenta
ZSH_HIGHLIGHT_STYLES[back-quoted-argument]=none
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-delimiter]=fg=blue,bold
ZSH_HIGHLIGHT_STYLES[single-quoted-argument]=fg=yellow
ZSH_HIGHLIGHT_STYLES[double-quoted-argument]=fg=yellow
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument]=fg=yellow
ZSH_HIGHLIGHT_STYLES[rc-quote]=fg=magenta
ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]=fg=magenta
ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]=fg=magenta
ZSH_HIGHLIGHT_STYLES[back-dollar-quoted-argument]=fg=magenta
ZSH_HIGHLIGHT_STYLES[assign]=none
ZSH_HIGHLIGHT_STYLES[redirection]=fg=blue,bold
ZSH_HIGHLIGHT_STYLES[comment]=fg=black,bold
ZSH_HIGHLIGHT_STYLES[named-fd]=none
ZSH_HIGHLIGHT_STYLES[numeric-fd]=none
ZSH_HIGHLIGHT_STYLES[arg0]=fg=green
ZSH_HIGHLIGHT_STYLES[bracket-error]=fg=red,bold
ZSH_HIGHLIGHT_STYLES[bracket-level-1]=fg=blue,bold
ZSH_HIGHLIGHT_STYLES[bracket-level-2]=fg=green,bold
ZSH_HIGHLIGHT_STYLES[bracket-level-3]=fg=magenta,bold
ZSH_HIGHLIGHT_STYLES[bracket-level-4]=fg=yellow,bold
ZSH_HIGHLIGHT_STYLES[bracket-level-5]=fg=cyan,bold
ZSH_HIGHLIGHT_STYLES[cursor-matchingbracket]=standout

PROMPT_EOL_MARK=""

eval "$(starship init zsh)"

export ZSH="$HOME/.oh-my-zsh"
# ZSH_THEME="spaceship"
# ZSH_THEME="robbyrussell"
source $ZSH/oh-my-zsh.sh

source $(dirname $(gem which colorls))/tab_complete.sh

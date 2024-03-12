
# Autostart startx
if [ "$(tty)" = "/dev/tty1" ]; then
	startx &> /home/caracole/.startx.log
	# setxkbmap -option "nbsp:none"
fi

export ZSH="$HOME/.oh-my-zsh"
# ZSH_THEME="spaceship"
# ZSH_THEME="robbyrussell"
source $ZSH/oh-my-zsh.sh

export PATH=$PATH:/home/caracole/.local/bin:/usr/local/sbin:/usr/sbin:/home/caracole/.local/share/fnm

# Commenté parce que ça prend un temps de malade au chargement
#export NVM_DIR="$HOME/.nvm"
#[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
#[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# export FZF_COMPLETION_TRIGGER=';;'
export FZF_DEFAULT_COMMAND="rg --hidden --ignore-case --files"
alias f='vim $(fzf --reverse --multi --cycle --scroll-off 2 --border none --prompt " " --pointer "" --marker "" --preview "batcat --pager never --color always --style auto {}" --height 50%)'

alias ls="logo-ls"

alias zshrc="vim ~/.zshrc"
alias vimrc="vim ~/.vimrc"
alias i3config="vim ~/.config/i3/config"

alias l="ls -lAh"
alias la="ls -A"
alias lld="ls -dlh"

alias update="sudo apt update && sudo apt --with-new-pkgs upgrade && sudo apt autoremove && sudo apt autoclean"

alias word="wc -w"
alias lines="wc -l"
alias maxlines="wc -L"

alias update_date="sudo ntpdate fr.pool.ntp.org"
alias clear_hist="echo '' > ~/.zsh_history"
alias clear_python="echo '' > ~/.python_history"
alias update_pip="pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U"
alias update_polybar="~/.config/polybar/launch.sh --forest 2>/dev/null"

alias rmd="rm -rf"
alias whois="whois -H"
alias nmap_fast="nmap -F -T5 --version-light --top-ports 300"
alias nmap_local="nmap_fast 192.168.0.0-255"

alias inst="sudo apt install"
alias rem="sudo apt remove"
alias purge="sudo apt purge"
alias search="sudo apt search"
alias show="sudo apt show"

alias feveryw="sudo find /* 2>/dev/null | grep"
alias dirsize="du -h --max-depth=0"

alias mandelbulber_render="cd /home/caracole/mandelbulber/animation/ && cat *.jpg | ffmpeg -framerate 1 -f image2pipe -i - -c:v libx264 -r 30 -pix_fmt yuv420p output.mp4 && mv output.mp4 /home/caracole/Vidéos/"
alias change_bg="nitrogen --set-zoom-fill --random /home/caracole/Images/wallpaper/"
alias change_dual="nitrogen --set-zoom-fill --random /home/caracole/Images/dual wallpaper/"
alias dual_screen="xrandr --auto --output HDMI-1-0 --mode 1920x1080 --right-of eDP-1 && nitrogen --set-zoom-fill --random /home/caracole/Images/dual wallpaper/ && i3-msg restart"
alias single_screen="xrandr --output HDMI-1-0 --off && nitrogen --set-zoom-fill --random /home/caracole/Images/wallpaper/ && i3-msg restart"
alias discipline_bg="nitrogen --set-zoom-fill --random /home/caracole/Images/wallpaper/discipline.jpg"

alias c="clear"

alias get_perf="sudo cpupower info -b"
alias set_perf="sudo cpupower set -b"
alias add_ram="sudo swapoff -a && sleep 10 && sudo swapon -a && sudo swapon /swapfile && sudo sysctl -w vm.min_free_kbytes=78993 && sudo sysctl -w vm.swappiness=10"


alias csdj="pactl load-module module-null-sink sink_name='virtual_speaker' sink_properties=device.description='virtual_speaker' && pactl load-module module-remap-source master='virtual_speaker.monitor' source_name='virtual_mic' source_properties=device.description='virtual_mic'"
alias close_csdj="pactl unload-module module-null-sink"
# IMPORTANT LES COMMANDES POUR CHANGER TON KERNEL SONT LES SUIVANTES :
# export UUID=$(sudo blkid -s UUID -o value /dev/nvme0n1p8)
# sudo efibootmgr -c -g -L "Debian EFIStub" --disk /dev/nvme0n1 -l '\EFI\Debian\vmlinuz' -u "root=UUID=$UUID rw quiet splash snd-intel-dspcfg.dsp_driver=1 ignore_dmi=1 rootfstype=ext4 add_efi_memmap initrd=\\EFI\\Debian\\initrd.img" PUIS ENSUITE, TU CHOISIS DANS LE BIOS LE NOM QUE T'AS MIS ET DU SUPPRIME L'ANCIEN

# Pour lancer un script avec la carte Nvidia :
# __NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia

setopt autocd
setopt interactivecomments
setopt notify
setopt hist_ignore_space
setopt AUTO_PUSHD
setopt CD_SILENT
setopt APPEND_HISTORY
setopt HIST_VERIFY
setopt SHARE_HISTORY

autoload compinit
compinit

. /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
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

# fnm
eval "`fnm env`"

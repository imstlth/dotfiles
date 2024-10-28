if status is-interactive
    # Commands to run in interactive sessions can go here
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

# LES COMMANDES POUR CHANGER TON KERNEL RESTENT (en gros) LES MÊMES QUE SUR ZSH
# export UUID=$(sudo blkid -s UUID -o value /dev/nvme0n1p2)
# sudo efibootmgr --create --disk /dev/nvme0n1 --part 1 --label "Arch Linux" --loader '\EFI\ArchLinux\vmlinuz-linux' -u "root=UUID=$UUID rw quiet loglevel=3 snd-intel-dspcfg.dsp_driver=3 nvidia_drm.modeset=1 initrd=\\EFI\\ArchLinux\\initramfs-linux.img"

# Pour lancer un script avec la carte Nvidia :
# prime-run glxinfo
# Ça le fait tout seul pour tous les scripts que tu lances via alacritty

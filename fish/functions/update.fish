function update
    sudo mount /dev/nvme0n1p1 /efi
    sudo pacman -Syu
    yay -Syu
    sudo pacman -Qdtq | sudo pacman -Rs -
    yay -Sc
    sudo cp -af /boot/vmlinuz-linux /efi/EFI/ArchLinux/
    sudo cp -af /boot/initramfs-linux.img /efi/EFI/ArchLinux/
    sudo umount /efi
end

# Si ça fait une erreur du style "argument « - » spécifié machin" c'est qu'il n'y a rien à clear
function clear_dep
    sudo pacman -Qdtq | sudo pacman -Rs -
end

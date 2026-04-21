function clear_cache
    mv ~/.cache/bat/ ~/
    rm -rf ~/.cache/
    mkdir -p ~/.cache/
    mv ~/bat/ ~/.cache/
    sudo rm -rf /var/cache/
    fc-cache -fv
end

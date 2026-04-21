function dotfiles
    cd ~
    mv .git_/ .git/
    git add .
    read -P "message du commit: " message
    git commit -m $message
    ccat Documents/txt/git_token.cpt
    echo "Une fois que t'as copié ton mdp, appuis sur entrée pour passer à la suite"
    read -P ""
    echo "ton username est 'imstlth'"
    git push --set-upstream main main
    mv .git/ .git_/
    echo "Fini !"
end

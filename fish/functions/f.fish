function f
    fzf --reverse --border rounded --walker file,hidden -i --cycle --bind 'enter:become(nvim {})' --scroll-off 2 --prompt ' ' --pointer '' --marker '' --preview "bat --pager never --color always --style auto {} --theme tokyonight" --scheme path  --color 'fg:#c0caf5,bg:#1a1b26,gutter:#1a1b26,fg+:#c0caf5,bg+:#292e42,hl+:#ff9e64,info:#7aa2f7,prompt:#7dcfff,pointer:#7dcfff,marker:#9ece6a,spinner:#9ece6a,header:#9ece6a,query:cyan,hl:magenta'
end

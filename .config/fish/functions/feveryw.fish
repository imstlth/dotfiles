function feveryw
    sudo find / -path /usr/share/icons -prune -o -print 2>/dev/null | grep -i $argv
end

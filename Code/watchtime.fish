#!/bin/fish
cat /home/caracole/.watchtime | read minutes date
set currdate (date +'%d')
if not test "$date" = "$currdate"
  set -g minutes 0
end
set date $currdate

while true
  while contains steam $(ps -A)
    set minutes (math $minutes + 1)
    echo $minutes $date > /home/caracole/.watchtime
    sleep 60
    if test "$minutes" -gt 180
      notify-send --app-name='Contrôle du temps' -u critical --icon=/usr/share/icons/Adwaita/scalable/devices/input-gaming.svg "Steam" "Tu as dépassé 3h de jeu aujourd'hui, tu dois faire autre chose jusqu'à demain."
    end
  end
  sleep 120
end

#!/bin/fish

set choix $(echo "   Shutdown
󰑓   Reboot
󰒲   Sleep" | rofi -dmenu)

switch $choix
case "   Shutdown"
  shutdown now
case "󰑓   Reboot"
  reboot
case "󰒲   Sleep"
  notify-send "Ça marche"
end

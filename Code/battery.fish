#!/bin/fish
while true
  if test "$(cat /sys/class/power_supply/BAT0/capacity)" -lt 15 && not test "$(cat /sys/class/power_supply/BAT0/status)" = "Charging"
    dunstify -I "/usr/share/icons/Papirus/22x22/panel/battery-000.svg" -a "System" -u critical "Battery" "Please charge." -h string:x-dunst-stack-tag:"battery"
  end
  sleep 20
end

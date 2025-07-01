#!/bin/fish
while true
  if test "$(cat /sys/class/power_supply/BAT0/capacity)" -lt 15 && not test "$(cat /sys/class/power_supply/BAT0/status)" = "Charging"
    notify-send -a "Ouh là" -u critical -w "La batterie dit" "Il faut charger !"
  end
  sleep 20
end

#!/bin/fish
echo $(math "$(cat /sys/class/backlight/intel_backlight/actual_brightness)" + 6000) > /sys/class/backlight/intel_backlight/brightness

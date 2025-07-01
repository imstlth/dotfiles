#!/bin/fish
for dir in /sys/class/hwmon/*
  if test "$(cat $dir/name)" = "coretemp"
    echo "$(math (cat $dir/temp1_input) / 1000)"°C
  end
end

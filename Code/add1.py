#!/bin/python3
import datetime as dt
import time
import os
import sys
import locale

locale.setlocale(locale.LC_TIME, "fr_FR.utf8")


DELTA = dt.timedelta(0, 0, 0, 0, 0, 3)

datafile = open("/home/caracole/.data", "r")
data = eval(datafile.read())
count, last_secs, prev_inter = data
prev_inter = dt.timedelta(seconds=prev_inter)
datafile.close()

last_date = dt.datetime.fromtimestamp(last_secs)
diff = dt.datetime.now() - last_date

if sys.argv[1] == "check":
    if prev_inter > diff:
        symbol = "  "
    else:
        symbol = "  "
    print(f"{count} | {diff.days} {symbol}")
elif sys.argv[1] == "info":
    next_str = (last_date + prev_inter).strftime("%a %d %b %Y à %H:%M")
    os.system("notify-send -a 'prochaine fois' -w 'pas avant' '" + next_str + "'")
else:
    inter = diff + DELTA
    if prev_inter > diff:
        os.system("notify-send -a 'TROP GUEZ' 'aucune volonté'")
    next_str = (dt.datetime.now() + inter).strftime("%a %d %b %Y à %H:%M")
    os.system("notify-send -a 'prochaine fois' -w 'pas avant' '" + next_str + "'")
    datafile = open("/home/caracole/.data", "w")
    datafile.write(repr([count + 1, int(time.time()), int(inter.total_seconds())]))
    datafile.close()

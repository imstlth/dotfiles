function ttv
    streamlink --player mpv --twitch-low-latency https://www.twitch.tv/$argv[1] best
end

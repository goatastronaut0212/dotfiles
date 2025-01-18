from libqtile import hook, qtile

@hook.subscribe.startup
def autostart():
    qtile.spawn("ibus-daemon -drx")
    qtile.spawn("picom")
    qtile.spawn("blueman-applet")

#!/usr/bin/python3

import openrazer.client

a = openrazer.client.DeviceManager()
a.turn_off_on_screensaver = False
for device in a.devices:
    device.poll_rate = 1000
    if device.type == "mouse":
        device.brightness = 90
        device.fx.static(255, 0, 0)  # hex thumb keys colors
        device.fx.misc.logo.breath_single(0,255,0)  # The logo's colors
        device.fx.misc.scroll_wheel.static(0,0,255)  # The scroll wheel's colors

# To change effects, play around with the numbers and effects
# There are options like .static(x,x,x) , .breath_dual( not sure how to use this, as the obvious way does not work ), .wave(), etc  
# Hopefully this helps anyone with this kind of issue
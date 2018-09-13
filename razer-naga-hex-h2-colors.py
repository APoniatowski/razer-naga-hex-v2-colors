#!/usr/bin/python3

import openrazer.client

a = openrazer.client.DeviceManager()
a.turn_off_on_screensaver = False
for device in a.devices:
    device.poll_rate = 1000
    if device.type == "mouse":
        device.brightness = 90
        device.fx.static(255, 0, 0)
        device.fx.misc.logo.breath_single(0,255,0)
        device.fx.misc.scroll_wheel.static(0,0,255) 

# To change effects, play around with the numbers and effects
# There are options like .static(x,x,x) , .breath_dual( not sure how to use this, as the obvious way does not work ), .wave(), etc  
# Hopefully this helps anyone with this kind of issue
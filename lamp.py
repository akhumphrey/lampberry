#!/usr/bin/env python

import unicornhat as unicorn
import time, math, colorsys
from os import system

i = 0.0
offset = 30
brightness = 1
brightness_step = 0.001
t = 0
idle_max = 20 * 60 * 100
sleep_per_cycle = 0.03
while True:
  i = i + 0.005

  if brightness <= 0.4:
    unicorn.off()
    time.sleep( idle_max / ( sleep_per_cycle * 1000 ) )
    system('shutdown -h now')
    break

  if t <= idle_max:
    t = t + 1
    #if t % 500 == 0:
    #  print 't:' + str(t) + '=>' + str(idle_max)
    #  pass
  
  if t > idle_max:
    brightness = brightness - brightness_step
    #print 'brightness:' + str(brightness)
    unicorn.brightness( brightness )

  r = (math.cos((i)/2.0) + math.cos((i)/2.0)) * 64.0 + 128.0
  g = (math.sin((i)/1.5) + math.sin((i)/2.0)) * 64.0 + 128.0
  b = (math.sin((i)/2.0) + math.cos((i)/1.5)) * 64.0 + 128.0

  r = max(0, min(255, r + offset))
  g = max(0, min(255, g + offset))
  b = max(0, min(255, b + offset))

  for y in range(8):
    for x in range(8):
      unicorn.set_pixel(x, y, int(r), int(g), int(b))
      
  unicorn.show()
  time.sleep(sleep_per_cycle)

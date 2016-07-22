#!/usr/bin/env python

import itertools
import math
import os
import time

import unicornhat as unicorn


def clamp_to_byte(value, lower_bound=0, upper_bound=255):
    """Clamps a number between bounds, rounds it and converts to int."""
    if value < lower_bound:
        return lower_bound
    if value > upper_bound:
        return upper_bound
    return int(round(value))


def set_hat_color(hue, level_boost=0):
    """Updates the unicorn with a uniform color."""
    r = (math.cos(hue / 2) * 2) * 64 + level_boost
    g = (math.sin(hue / 1.5) + math.sin(hue / 2)) * 64 + level_boost
    b = (math.sin(hue / 2) + math.cos(hue / 1.5)) * 64 + level_boost

    for x, y in itertools.product(range(8), repeat=2):
        unicorn.set_pixel(x, y, *map(clamp_to_byte, (r, g, b)))
    unicorn.show()


def main(
        offset=30,
        brightness=1,
        brightness_step=0.001,
        brightness_shutoff=0.4,
        tick_max=120000,
        cycle_period=0.03,
        hue_step=0.005):
    offset = offset + 128
    for tick in itertools.count():
        cycle_end = time.time() + cycle_period

        if brightness <= brightness_shutoff:
            unicorn.off()
            time.sleep(tick_max / cycle_period / 1000)
            os.system('shutdown -h now')

        if tick > tick_max:
            brightness -= brightness_step
            unicorn.brightness(brightness)

        set_hat_color(tick * hue_step, level_boost=offset)
        time.sleep(max(time.time() - cycle_end, 0))


if __name__ == '__main__':
    main()

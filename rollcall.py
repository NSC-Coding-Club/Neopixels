#!/usr/bin/env python

import time
import random

import board
import neopixel
import numpy as np

# LED strip configuration:
LED_COUNT   = 372      # Number of LED pixels.
LED_PIN     = board.D12      # GPIO pin
LED_BRIGHTNESS = 0.2  # LED brightness
LED_ORDER = neopixel.GRB # order of LED colours. May also be RGB, GRBW, or RGBW

colours_array = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,105,180),(192,192,192)]

# Create NeoPixel object with appropriate configuration.
strip = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness = LED_BRIGHTNESS, auto_write=False, pixel_order = LED_ORDER)

# Create a way to fade/transition between colours using numpy arrays

def fade(colour1, colour2, percent):
    colour1 = np.array(colour1)
    colour2 = np.array(colour2)
    vector = colour2-colour1
    newcolour = (int((colour1 + vector * percent)[0]), int((colour1 + vector * percent)[1]), int((colour1 + vector * percent)[2]))
    return newcolour

# Create a function that will cycle through the colours selected above
	
def rollcall_cycle(wait):
    for j in range(len(colours_array)):
        for i in range(10):
            colour1 = colours_array[j]
            if j == 5:
                colour2 = (255,255,255)
            else:
                colour2 = colours_array[(j+1)]
            percent = i*0.1   # 0.1*100 so 10% increments between colours
            strip.fill((fade(colour1,colour2,percent)))
            strip.show()
            time.sleep(wait)

def single_colour_chase(colour, wait):
    for p in range(0, LED_COUNT-16, 5):
        strip[p]=colour
        strip[p+4]=colour
        strip[p+8]=colour
        strip[p+12]=colour
        strip[p+16]=colour
        strip.show()
        time.sleep(wait)
        strip.fill((0,0,0))
        strip.show

def dual_colour_chase(colour1, colour2, wait):
    for p in range(0, LED_COUNT-12, 4):
        strip[p]=colour1
        strip[p+4]=colour1
        strip[p+8]=colour1
        strip[p+12]=colour1
        strip[LED_COUNT-p-1]=colour2
        strip[LED_COUNT-p-5]=colour2
        strip[LED_COUNT-p-9]=colour2
        strip[LED_COUNT-p-13]=colour2
        strip.show()
        time.sleep(wait)
        strip.fill((0,0,0))
        strip.show


 
#strip.fill((255,255,255))
#strip.show()

# Main function loop

while True:

    choice = random.randint(1,3)

    if choice == 1:
         rollcall_cycle(0.2)    # 0.2 seconds between colour updates
    elif choice == 2:
         single_colour_chase((random.randint(0,255),random.randint(0,255),random.randint(0,255)), random.random()*0.06)
         single_colour_chase((random.randint(0,255),random.randint(0,255),random.randint(0,255)), random.random()*0.06)
         single_colour_chase((random.randint(0,255),random.randint(0,255),random.randint(0,255)), random.random()*0.06)
         single_colour_chase((random.randint(0,255),random.randint(0,255),random.randint(0,255)), random.random()*0.06)
    elif choice == 3:
         dual_colour_chase((random.randint(0,255),random.randint(0,255),random.randint(0,255)),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),random.random()*0.06)
         dual_colour_chase((random.randint(0,255),random.randint(0,255),random.randint(0,255)),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),random.random()*0.06)
         dual_colour_chase((random.randint(0,255),random.randint(0,255),random.randint(0,255)),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),random.random()*0.06)
         dual_colour_chase((random.randint(0,255),random.randint(0,255),random.randint(0,255)),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),random.random()*0.06)

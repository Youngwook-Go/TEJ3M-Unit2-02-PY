"""
Created by: Youngwook Go
Created on: Sep 2023
Blinks Arduino Pico Built-In LED for increasing time
"""

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

blinkTime = 1

while True:
	led.value = True
	time.sleep(blinkTime)
	led.value = False
	time.sleep (1)
	blinkTime = blinkTime + 1

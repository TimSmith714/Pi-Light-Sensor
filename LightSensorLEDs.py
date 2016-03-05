#Some code from the Adafruit website at http://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading

#Adafruit Code
#!usr/bin/env python

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier versions
# are not fast enough!

import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)

#My addition for LEDs
RED = 17
GREEN = 22
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
#End my code

def RCtime (RCpin):
  reading = 0
  GPIO.setup(RCpin, GPIO.OUT)
  GPIO.output(RCpin, GPIO.LOW)
  time.sleep(0.1)
  
  GPIO.setup(RCpin, GPIO.IN)
  # This takes about 1 millisecond per loop cycle
  while (GPIO.input(RCpin) == GPIO.LOW):
    reading += 1
  return reading
  
while True:
  print RCtime(18) # Read RC timing using pin #18
  
  #Begin my code for the LEDs
  if RCtime(18) < 1000:
    GPIO.output(RED, True)
    GPIO.output(GREEN, False)
  elif RCtime(18) > 1000:
    GPIO.output(RED, False)
    GPIO.output(GREEN, True)
  else:
    GPIO.output(RED, False)
    GPIO.output(GREEN, False)
  #End my code


#!/usr/bin/env python3
"""
  ColorLED.py
  The colorful searchlight will switch to different colors every second.

  NOTE: After terminating the program, the state of the relevant pin is uncertain
  so we need to run a script to initialize all pins (initpin.sh).
"""
import RPi.GPIO as GPIO
import time

# Definition of RGB module pin
LED_R = 22
LED_G = 27
LED_B = 24

# Set the GPIO port to BCM encoding mode.
GPIO.setmode(GPIO.BCM)

# RGB pins are initialized to output mode
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

# Display 7 color LED
try:
    while True:
        # Red
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.LOW)
        time.sleep(1)

        # Green
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.LOW)
        time.sleep(1)

        # Blue
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        time.sleep(1)

        # Yellow
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.LOW)
        time.sleep(1)

        # Fuchsia
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        time.sleep(1)

        # Aqua
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.HIGH)
        time.sleep(1)

        # Black (off)
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.LOW)
        time.sleep(1)
except:
    print("except")

GPIO.cleanup()

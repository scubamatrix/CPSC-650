#!/usr/bin/env python3
"""
  ServoControlColorVersion2.py
  The servo starts to turn and lights up different colors
  when turning to different angles.
  This code uses its own defined pulse function to generate pwm waveform

  NOTE: After terminating the program, the state of the relevant pin is uncertain
  so we need to run a script to initialize all pins (initpin.sh).
"""
import RPi.GPIO as GPIO
import time

# Definition of RGB module pins
LED_R = 22
LED_G = 27
LED_B = 24

# Definition of servo pin
ServoPin = 23

# Set the GPIO port to BCM encoding mode.
GPIO.setmode(GPIO.BCM)

# Ignore warning information
GPIO.setwarnings(False)


def init():
    """
    RGB module pins are initialized into output mode
    Servo pin is initialized into input mode
    """
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)
    GPIO.setup(ServoPin, GPIO.OUT)


def servo_pulse(myangle):
    """
    Define a pulse function to generate the PWM value in the analog mode.
    The base pulse is 20ms, and the high level of the pulse is controlled
    at 0-180 degrees in 0.5-2.5ms.
    """
    pulsewidth = (myangle * 11) + 500
    GPIO.output(ServoPin, GPIO.HIGH)
    time.sleep(pulsewidth/1000000.0)
    GPIO.output(ServoPin, GPIO.LOW)
    time.sleep(20.0/1000-pulsewidth/1000000.0)


def corlor_light(pos):
    """
    The servo turns from 0-180, then turns from 180 to 0.
    At the same time, the 180 degree angle is divided into 7 sections
    to represent 7 different colors.
    """
    if pos > 150:
        GPIO.output(LED_R, GPIO.HIGH)
    	GPIO.output(LED_G, GPIO.LOW)
    	GPIO.output(LED_B, GPIO.LOW)
    elif pos > 125:
    	GPIO.output(LED_R, GPIO.LOW)
    	GPIO.output(LED_G, GPIO.HIGH)
    	GPIO.output(LED_B, GPIO.LOW)
    elif pos > 100:
        GPIO.output(LED_R, GPIO.LOW)
    	GPIO.output(LED_G, GPIO.LOW)
    	GPIO.output(LED_B, GPIO.HIGH)
    elif pos > 75:
    	GPIO.output(LED_R, GPIO.HIGH)
    	GPIO.output(LED_G, GPIO.HIGH)
    	GPIO.output(LED_B, GPIO.LOW)
    elif pos > 50:
    	GPIO.output(LED_R, GPIO.LOW)
    	GPIO.output(LED_G, GPIO.HIGH)
    	GPIO.output(LED_B, GPIO.HIGH)
    elif pos > 25:
        GPIO.output(LED_R, GPIO.HIGH)
    	GPIO.output(LED_G, GPIO.LOW)
    	GPIO.output(LED_B, GPIO.HIGH)
    elif pos > 0:
        GPIO.output(LED_R, GPIO.HIGH)
    	GPIO.output(LED_G, GPIO.HIGH)
    	GPIO.output(LED_B, GPIO.HIGH)
    else:
        GPIO.output(LED_R, GPIO.LOW)
    	GPIO.output(LED_G, GPIO.LOW)
    	GPIO.output(LED_B, GPIO.LOW)


def servo_control_color():
    for pos in range(181):
        servo_pulse(pos)
	corlor_light(pos)
	time.sleep(0.009)
    for pos in reversed(range(181)):
        servo_pulse(pos)
	corlor_light(pos)
	time.sleep(0.009)


# Wait 2 sec
time.sleep(2)

# The try/except statement is used to detect errors in the try block.
# The except statement catches the exception information and processes it.
try:
    init()
    while True:
        servo_control_color()
except KeyboardInterrupt:
    pass

GPIO.cleanup()

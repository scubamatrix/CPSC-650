#!/usr/bin/env python3
"""
  KeyScanStart.py
  When the KEY is pressed to start the car,
  the car will advance 1 s, back 1 s, turn left 2 s, turn right 2 s,
  turn left in place 3 s, turn right in place 3 s, stop 0.5s.

  NOTE: After terminating the program, the state of the relevant pin is uncertain
  so we need to run a script to initialize all pins (initpin.sh).
"""
import RPi.GPIO as GPIO
import time

#Definition of  motor pin
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

#Definition of  key
key = 8

#Set the GPIO port to BCM encoding mode
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)


def motor_init():
    """
    Motor pins are initialized into output mode
    Key pin is initialized into input mode
    """
    global pwm_ENA
    global pwm_ENB
    global delaytime
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
    #Set the PWM pin and frequency is 2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)
    GPIO.setup(key, GPIO.IN)


def run(delaytime):
    """
    Move forward (advance)
    """
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)
    time.sleep(delaytime)


def back(delaytime):
    """
    Move backward
    """
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)
    time.sleep(delaytime)


def left(delaytime):
    """
    Turn left
    """
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)
    time.sleep(delaytime)


def right(delaytime):
    """
    Turn right
    """
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)
    time.sleep(delaytime)


def spin_left(delaytime):
    """
    Turn left in place
    """
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)
    time.sleep(delaytime)


def spin_right(delaytime):
    """
    Turn right in place
    """
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)
    time.sleep(delaytime)


def brake(delaytime):
    """
    Brake (stop)
    """
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)
    time.sleep(delaytime)


def key_scan():
    """
    Button detection
    """
    while GPIO.input(key):
        pass
    while not GPIO.input(key):
        time.sleep(0.01)
	if not GPIO.input(key):
	    time.sleep(0.01)
	    while not GPIO.input(key):
	        pass


# Delay 2s
time.sleep(2)

# The try/except statement is used to detect errors in the try block.
# the except statement catches the exception information and processes it.
try:
    motor_init()
    key_scan()
    while True:
        run(1)
	back(1)
	left(2)
	right(2)
	spin_left(3)
	spin_right(3)
	brake(1)
except KeyboardInterrupt:
    pass

pwm_ENA.stop()
pwm_ENB.stop()
GPIO.cleanup()

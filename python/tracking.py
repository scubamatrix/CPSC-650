#!/usr/bin/env python3
"""
  tracking.py
  After running the program, press the K2 to start the car.
  The tracking function is started.
  The robot car will automatically walk along the black line.

  NOTE: After terminating the program, the state of the relevant pin is uncertain
  so we need to run a script to initialize all pins (initpin.sh).
"""
import RPi.GPIO as GPIO
import time

# Definition of  motor pins
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

# Definition of  button
key = 8

# TrackSensorLeftPin1 TrackSensorLeftPin2 TrackSensorRightPin1 TrackSensorRightPin2
#      3                 5                  4                   18
# The first tracking infrared sensor pin on the left is connected to  BCM port 3 of Raspberry pi
TrackSensorLeftPin1 = 3
# The second tracking infrared sensor pin on the left is connected to  BCM port 5 of Raspberry pi
TrackSensorLeftPin2 = 5
# The first tracking infrared sensor pin on the right is connected to  BCM port 4 of Raspberry pi
TrackSensorRightPin1 = 4
# The second tracking infrared sensor pin on the right is connected to  BCMport 18 of Raspberry pi
TrackSensorRightPin2 = 18

# Set the GPIO port to BCM encoding mode.
GPIO.setmode(GPIO.BCM)

# Ignore warning information
GPIO.setwarnings(False)


def init():
    """
    Motor pins are initialized into output mode
    Key pin is initialized into input mode
    Track sensor module pins are initialized into input mode
    """
    global pwm_ENA
    global pwm_ENB
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(key, GPIO.IN)
    GPIO.setup(TrackSensorLeftPin1, GPIO.IN)
    GPIO.setup(TrackSensorLeftPin2, GPIO.IN)
    GPIO.setup(TrackSensorRightPin1, GPIO.IN)
    GPIO.setup(TrackSensorRightPin2, GPIO.IN)
    # Set the PWM pin and frequency is 2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)


def run(leftspeed, rightspeed):
    """
    Move forward (advance)
    """
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)


def back(leftspeed, rightspeed):
    """
    Move backward
    """
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)


def left(leftspeed, rightspeed):
    """
    Turn left
    """
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)


def right(leftspeed, rightspeed):
    """
    Turn right
    """
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)


def spin_left(leftspeed, rightspeed):
    """
    Turn left in place
    """
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)


def spin_right(leftspeed, rightspeed):
    """
    Turn right in place
    """
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)


def brake():
    """
    Brake (stop)
    """
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)


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
    init()
    key_scan()
    while True:
        # When the black line is detected, the corresponding indicator of the tracking module is on, and the port level is LOW.
        # When the black line is not detected, the corresponding indicator of the tracking module is off, and the port level is HIGH.
        TrackSensorLeftValue1 = GPIO.input(TrackSensorLeftPin1)
        TrackSensorLeftValue2 = GPIO.input(TrackSensorLeftPin2)
        TrackSensorRightValue1 = GPIO.input(TrackSensorRightPin1)
        TrackSensorRightValue2 = GPIO.input(TrackSensorRightPin2)

        # 4 tracking pins level status
        # 0 0 X 0
        # 1 0 X 0
        # 0 1 X 0
        # Turn right in place,speed is 100,delay 80ms
        # Handle right acute angle and right right angle
        if (TrackSensorLeftValue1 == False or TrackSensorLeftValue2 == False) and TrackSensorRightValue2 == False:
            spin_right(35, 35)
        time.sleep(0.08)

        # 4 tracking pins level status
        # 0 X 0 0
        # 0 X 0 1
        # 0 X 1 0
        # Turn right in place,speed is 100,delay 80ms
        # Handle left acute angle and left right angle
        elif TrackSensorLeftValue1 == False and (TrackSensorRightValue1 == False or TrackSensorRightValue2 == False):
            spin_left(35, 35)
            time.sleep(0.08)

        # 0 X X X
        # Left_sensor1 detected black line
        elif TrackSensorLeftValue1 == False:
            spin_left(35, 35)

        # X X X 0
        # Right_sensor2 detected black line
        elif TrackSensorRightValue2 == False:
            spin_right(35, 35)

        # 4 tracking pins level status
        # X 0 1 X
        elif TrackSensorLeftValue2 == False and TrackSensorRightValue1 == True:
            left(0, 40)

        # 4 tracking pins level status
        # X 1 0 X
        elif TrackSensorLeftValue2 == True and TrackSensorRightValue1 == False:
            right(40, 0)

        # 4 tracking pins level status
        # X 0 0 X
        elif TrackSensorLeftValue2 == False and TrackSensorRightValue1 == False:
            run(50, 50)

        # When the level of 4 pins are 1 1 1 1, the car keeps the previous running state.

except KeyboardInterrupt:
    pass

pwm_ENA.stop()
pwm_ENB.stop()
GPIO.cleanup()

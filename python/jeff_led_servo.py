#!/usr/bin/env python3
"""
  jeff_led_servo.py
  The servo starts to turn and lights up while turning to different angles.
"""
import RPi.GPIO as GPIO
import time

# Definition of RGB module pins
LED_R = 22
LED_G = 27
LED_B = 24

# Definition of servo pin
ServoPin = 23

# Definition of motor pins
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

# Definition of key
key = 8

# Definition of ultrasonic module pins
EchoPin = 0
TrigPin = 1

# Set the GPIO port to BCM encoding mode
GPIO.setmode(GPIO.BCM)

# Ignore warning information
GPIO.setwarnings(False)


def servo_init():
    """
    RGB module pins are initialized into output mode
    Servo pin is initialized into input mode
    """
    global pwm_servo

    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)
    GPIO.setup(ServoPin, GPIO.OUT)

    pwm_servo = GPIO.PWM(ServoPin, 50)
    pwm_servo.start(0)


def color_light(pos):
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
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos / 180)
        color_light(pos)
        time.sleep(0.009)
    for pos in reversed(range(181)):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos / 180)
        color_light(pos)
        time.sleep(0.009)


def main():
    """
    The servo starts to turn and lights up
    while turning to different angles.
    """
    # Wait 2s
    time.sleep(2)

    # The try/except statement is used to detect errors in the try block.
    # the except statement catches the exception information and processes it.
    try:
        servo_init()
        pwm_servo.ChangeDutyCycle(2.5 + 10 * 90 / 180)
        while True:
            servo_control_color()
    except KeyboardInterrupt:
        pass

    pwm_servo.stop()
    GPIO.cleanup()


if __name__ == "__main__":
    main()

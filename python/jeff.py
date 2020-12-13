#!/usr/bin/env python3
"""
  jeff.py
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


def led_init():
    # RGB pins are initialized to output mode
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)


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


# ==========================


def motor_init():
    """
    Motor pin initialization operation
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
    # Set the PWM pin and frequency is 2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)


def run(leftspeed=50, rightspeed=50):
    """
    Move forward (advance)
    """
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
    # time.sleep(delaytime)


def back(leftspeed=50, rightspeed=50):
    """
    Move backward
    """
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
    # time.sleep(delaytime)


def left(leftspeed=50, rightspeed=50):
    """
    Turn left
    """
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
    # time.sleep(delaytime)


def right(leftspeed=50, rightspeed=50):
    """
    Turn right
    """
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
    # time.sleep(delaytime)


def spin_left(leftspeed=50, rightspeed=50):
    """
    Turn left in place
    """
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
    # time.sleep(delaytime)


def spin_right(leftspeed=50, rightspeed=50):
    """
    Turn right in place
    """
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
    # time.sleep(delaytime)


def brake():
    """
    Brake
    """
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    # time.sleep(delaytime)


# ==========================


def car_run():
    """
    The car will advance 1 s, back 1 s, turn left 2 s, turn right 2 s,
    spin left 3 s, spin right in place 3 s, stop 0.5s.
    """
    # Wait 2s
    time.sleep(2)

    # The try/except statement is used to detect errors in the try block.
    # the except statement catches the exception information and processes it.
    # The robot car will advance 1s，back 1s，turn left 2s，turn right 2s，
    # turn left in place 3s, turn right  in place 3s，stop 1s。
    try:
        motor_init()
        while True:
            run()
            time.sleep(1)
            back()
            time.sleep(1)
            left()
            time.sleep(2)
            right()
            time.sleep(2)
            spin_left()
            time.sleep(3)
            spin_right()
            time.sleep(3)
            brake()
            time.sleep(1)
    except (KeyboardInterrupt):
        pass

    pwm_ENA.stop()
    pwm_ENB.stop()
    GPIO.cleanup()


def color_led():
    """
    The colorful searchlight will switch to different colors every second.
    """
    led_init()

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
    except (Exception) as e:
        print(f"Unexpected error: {e}")

    GPIO.cleanup()


def servo_run():
    """
    The servo starts to turn and lights up different colors
    when turning to different angles.
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
    except (KeyboardInterrupt):
        pass

    pwm_servo.stop()
    GPIO.cleanup()


# ==========================


def servo_ultrasonic_init():
    """
    Motor pins are initialized into output mode
    Key pin is initialized into input mode
    Ultrasonic pin, RGB pin, and servo pin initialization
    """
    global pwm_ENA
    global pwm_ENB
    global pwm_servo
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(key, GPIO.IN)
    GPIO.setup(EchoPin, GPIO.IN)
    GPIO.setup(TrigPin, GPIO.OUT)
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)
    GPIO.setup(ServoPin, GPIO.OUT)
    # Set the PWM pin and frequency is 2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)

    pwm_servo = GPIO.PWM(ServoPin, 50)
    pwm_servo.start(0)


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


def distance():
    """
    Calculate distance (ultrasonic function)
    """
    GPIO.output(TrigPin, GPIO.LOW)
    time.sleep(0.000002)
    GPIO.output(TrigPin, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TrigPin, GPIO.LOW)

    t3 = time.time()

    while not GPIO.input(EchoPin):
        t4 = time.time()
        if (t4 - t3) > 0.03:
            return -1

    t1 = time.time()

    while GPIO.input(EchoPin):
        t5 = time.time()
        if (t5 - t1) > 0.03:
            return -1

    t2 = time.time()
    time.sleep(0.01)
    #    print "distance is %d " % (((t2 - t1)* 340 / 2) * 100)
    return ((t2 - t1) * 340 / 2) * 100


def distance_test():
    num = 0
    ultrasonic = []
    while num < 5:
        distance = distance()
        while int(distance) == -1:
            distance = distance()
            print("Tdistance is %f" % (distance))
        while int(distance) >= 500 or int(distance) == 0:
            distance = distance()
            print("Edistance is %f" % (distance))
        ultrasonic.append(distance)
        num = num + 1
        time.sleep(0.01)
    print(ultrasonic)
    distance = (ultrasonic[1] + ultrasonic[2] + ultrasonic[3]) / 3
    print("distance is %f" % (distance))
    return distance


def servo_appointed_detection(pos):
    """
    The servo rotates to the specified angle
    """
    for i in range(18):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos / 180)


def servo_color_carstate():
    """
    Calculate color of RGB module
    """
    # red
    GPIO.output(LED_R, GPIO.HIGH)
    GPIO.output(LED_G, GPIO.LOW)
    GPIO.output(LED_B, GPIO.LOW)
    back(20, 20)
    time.sleep(0.08)
    brake()

    servo_appointed_detection(0)
    time.sleep(0.8)
    rightdistance = distance_test()

    servo_appointed_detection(180)
    time.sleep(0.8)
    leftdistance = distance_test()

    servo_appointed_detection(90)
    time.sleep(0.8)
    frontdistance = distance_test()

    if leftdistance < 30 and rightdistance < 30 and frontdistance < 30:
        # Magenta
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        spin_right(85, 85)
        time.sleep(0.58)
    elif leftdistance >= rightdistance:
        # Blue
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        spin_left(85, 85)
        time.sleep(0.28)
    elif leftdistance <= rightdistance:
        # Magenta
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        spin_right(85, 85)
        time.sleep(0.28)


def servo_ultrasonic_run():
    # Wait 2s
    time.sleep(2)

    # The try/except statement is used to detect errors in the try block.
    # the except statement catches the exception information and processes it.
    try:
        init()
        key_scan()
        while True:
            distance = distance_test()
            if distance > 50:
                run(55, 55)
            elif 30 <= distance <= 50:
                run(45, 45)
            elif distance < 30:
                servo_color_carstate()

    except KeyboardInterrupt:
        pass

    pwm_ENA.stop()
    pwm_ENB.stop()
    GPIO.cleanup()


if __name__ == "__main__":
    # color_led()
    # car_run()
    # servo_run()
    servo_ultrasonic_run()

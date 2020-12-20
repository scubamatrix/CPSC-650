#!/usr/bin/env python3
"""
  jeff_avoid.py

  The ultrasonic obstacle avoidance with servo function is started.

  When there is an obstacle in front, the car can avoid the obstacle automatically.

  When the distance in front is less than 30cm, the colorful light module is red,
  then servo turns to 0 degree, ranging and recording, servo turns to 180 degree,
  ranging and recording, servo turns to 90 degree, ranging and recording.

  The robot car will compare the left and right distance to determine
  whether to avoid the obstacle to the left or right.

  When the distance in three directions is less than 30,
  the robot car will turn around.
"""
import RPi.GPIO as GPIO
import time

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

# Definition of RGB module pins
LED_R = 22
LED_G = 27
LED_B = 24

# Definition of servo pin
ServoPin = 23

# Set the GPIO port to BCM encoding mode
GPIO.setmode(GPIO.BCM)

# Ignore warning information
GPIO.setwarnings(False)


def init():
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
    Brake
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


# Ultrasonic function
"""
def Distance_test():
    GPIO.output(TrigPin,GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TrigPin,GPIO.LOW)
    while not GPIO.input(EchoPin):
        pass
    t1 = time.time()
    while GPIO.input(EchoPin):
        pass
    t2 = time.time()
    print "distance is %d " % (((t2 - t1)* 340 / 2) * 100)
    time.sleep(0.01)
    return ((t2 - t1)* 340 / 2) * 100
"""


def Distance():
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
    # print "distance is %d " % (((t2 - t1)* 340 / 2) * 100)
    time.sleep(0.01)

    return ((t2 - t1) * 340 / 2) * 100


def Distance_test():
    num = 0
    ultrasonic = []
    while num < 5:
        distance = Distance()

        while int(distance) == -1:
            distance = Distance()
            print("Tdistance is %f" % (distance))

        while int(distance) >= 500 or int(distance) == 0:
            distance = Distance()
            print("Edistance is %f" % (distance))

        ultrasonic.append(distance)
        num = num + 1
        time.sleep(0.01)

    distance = (ultrasonic[1] + ultrasonic[2] + ultrasonic[3]) / 3

    print("distance is %f" % (distance))
    return distance


def servo_appointed_detection(pos):
    """
    The servo rotates to the specified angle
    """
    for i in range(18):
        # This needs to be adjusted so that ultrasonic sensor is centered 
        pwm_servo.ChangeDutyCycle(1.5 + 10 * pos / 180)


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
    rightdistance = Distance_test()

    servo_appointed_detection(180)
    time.sleep(0.8)
    leftdistance = Distance_test()

    servo_appointed_detection(90)
    time.sleep(0.8)
    frontdistance = Distance_test()

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


if __name__ == "__main__":
    # Wait 2s
    time.sleep(2)

    # The try/except statement is used to detect errors in the try block.
    # the except statement catches the exception information and processes it.
    try:
        init()
        # key_scan()
        while True:
            distance = Distance_test()
            if distance > 50:
                run(35, 35)
            elif 15 <= distance <= 50:
                run(25, 25)
            elif distance < 15:
                servo_color_carstate()

    except KeyboardInterrupt:
        pass

    pwm_ENA.stop()
    pwm_ENB.stop()
    GPIO.cleanup()

#!/usr/bin/env python3
"""
  camera.py
  Take still pictures with Python code
  https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/5
"""
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (640, 480)
camera.start_preview()
sleep(3)
camera.capture('/home/jeff/Desktop/image.jpg')
camera.stop_preview()



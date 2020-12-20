#!/usr/bin/env python3
"""
  video.py
  Recording video with Python code
  https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/6
"""
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 15
camera.start_preview()
camera.start_recording('/home/jeff/Desktop/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()



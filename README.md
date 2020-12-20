# Robotics Term Project

This repo contains the source code for my term project for CPSC-65000 Robotics using [Raspberry Pi G1 Tank](https://github.com/YahboomTechnology/Raspberry-pi-G1-Tank) with Raspberry Pi 4 Model B and [Coral USB Accelerator](https://coral.ai/products/accelerator)

## [Coral Models](./coral)

This folder contains the Edge TPU models that are used in many of the code samples. Each [Edge TPU model](https://coral.ai/models/) provides a `.tflite` file that is pre-compiled to run on the Edge TPU.

## [OpenCV Sample Code](./opencv)

This folder contains code that uses camera streams together with the TensorFlow Lite API with a Coral device such as the USB Accelerator or Dev Board.

# [Raspberry-Pi-G1-Tank](./python)

This folder contains sample code from the [Raspberry-Pi-G1-Tank](https://github.com/YahboomTechnology/Raspberry-pi-G1-Tank) repository.

## [Python Quickstart](./quickstart)

This folder contains code that is based on the [Python quickstart](https://www.tensorflow.org/lite/guide/python) tutorial using TensorFlow Lite with Python for embedded devices based on Linux such as Raspberry Pi and Coral devices with Edge TPU.

## [Raspberry Pi camera module](./raspicam)

This folder contains code using the picamera library for Python to obtain camera images and perform image classification on the Edge TPU.

This code works on Raspberry Pi with the Pi Camera and Coral USB Accelerator.

---

## More Examples

[Coral Examples](https://coral.ai/examples/)

Code examples and project tutorials to build intelligent devices with Coral from the google-coral open source project for coral.ai

[TensorFlow Lite example apps](https://www.tensorflow.org/lite/examples)

A collection of TensorFlow Lite apps.

---

# Raspberry Pi camera example with Coral

This folder contains example code from the [Raspberry Pi camera example with Coral](https://github.com/google-coral/examples-camera/tree/master/raspicam) using the [picamera](https://github.com/google-coral/examples-camera/tree/master/raspicam) library for Python to obtain camera images and perform image classification on the Edge TPU.

This code works on Raspberry Pi with the Pi Camera and Coral USB Accelerator.

## Run the classification demo

```
  python3 classify_capture.py
```

By default, this uses the ```mobilenet_v2_1.0_224_quant_edgetpu.tflite``` model.

You can change the model and the labels file using flags ```--model``` and ```--labels```.

```
  python3 classify_capture.py \
    --model ../coral/models/mobilenet_v2_1.0_224_quant_edgetpu.tflite \
    --labels ../coral/labels/imagenet_labels.txt
```

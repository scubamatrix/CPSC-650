# Raspberry Pi camera example with Coral

This folder contains example code from the [Raspberry Pi camera example with Coral](https://github.com/google-coral/examples-camera/tree/master/raspicam) using the [picamera](https://github.com/google-coral/examples-camera/tree/master/raspicam) library for Python to obtain camera images and perform image classification on the Edge TPU.

This code works on Raspberry Pi with the Pi Camera and Coral USB Accelerator.

## Run the classification demo

```bash
  python3 classify_capture.py
```

By default, this uses the `mobilenet_v2_1.0_224_quant_edgetpu.tflite` model.

You can change the model and the labels file using flags `--model` and `--labels`.

```bash
  python3 classify_capture.py \
    --model ../coral/models/mobilenet_v2_1.0_224_quant_edgetpu.tflite \
    --labels ../coral/labels/imagenet_labels.txt
```

---

## More Examples

The [TensorFlow Lite Python classification example with Pi Camera](https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/raspberry_pi) uses TensorFlow Lite with Python on a Raspberry Pi to perform real-time image classification using images streamed from the Pi Camera.

```bash
    cd examples/lite/examples/image_classification/raspberry_pi

    python3 classify_picamera.py \
      --model /tmp/mobilenet_v1_1.0_224_quant_edgetpu.tflite \
      --labels /tmp/labels_mobilenet_quant_v1_224.txt
```

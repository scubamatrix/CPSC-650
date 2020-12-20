# OpenCV Sample Code

This folder contains code that uses camera streams together with the TensorFlow Lite API with a Coral device such as the USB Accelerator.

## OpenCV camera example with Coral

This folder contains example code from the [Edge TPU simple camera examples](https://github.com/google-coral/examples-camera) that uses OpenCV to obtain camera images and perform object detection on the Edge TPU.

This code works on Linux/macOS/Windows using a webcam, Raspberry Pi with the Pi Camera, and on the Coral Dev Board using the Coral Camera or a webcam. For all settings other than the Coral Dev Board, you also need a Coral USB/PCIe/M.2 Accelerator.

```bash
    # Run the program
    TEST_DATA=../all_models

    # Run face detection model (detects the location of human faces):
    python3 detect.py \
      --model ${TEST_DATA}/mobilenet_ssd_v2_face_quant_postprocess_edgetpu.tflite

    # Run coco model (detects the location of 90 types of objects):
    python3 detect.py \
      --model ${TEST_DATA}/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite \
      --labels ${TEST_DATA}/coco_labels.txt

    python3 detect.py \
        --model ../coral/models/ssd_mobilenet_v2_coco_quant_postprocess_edgetpu.tflite \
        --labels ../coral/labels/coco_labels.txt

    python3 classify_capture.py \
          --model ../coral/models/mobilenet_v2_1.0_224_quant_edgetpu.tflite \
          --labels ../coral/labels/imagenet_labels.txt
```

# OpenCV Sample Code

---

## [OpenCV camera examples with Coral](https://github.com/google-coral/examples-camera/tree/master/opencv)

Example code using OpenCV to obtain camera images and perform object detection on the Edge TPU.

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
        --model ../coral/models/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite \
        --labels ../coral/models/coco_labels.txt

    python3 classify_capture.py \
          --model ../coral/models/mobilenet_v2_1.0_224_quant_edgetpu.tflite \
          --labels ../coral/labels/imagenet_labels.txt
```

---

## [TensorFlow Lite Python classification example with Pi Camera](https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/raspberry_pi)

```bash
    cd examples/lite/examples/image_classification/raspberry_pi

    python3 classify_picamera.py \
      --model /tmp/mobilenet_v1_1.0_224_quant_edgetpu.tflite \
      --labels /tmp/labels_mobilenet_quant_v1_224.txt
```

---

## [Models Built for the Edge TPU](https://coral.ai/models/)

MobileNet SSD v2 (COCO)

- Detects the location of 90 types of objects
- Dataset: COCO
- Input size: 300x300

MobileNet SSD v2 (Faces)

- Detects the location of human faces
- Dataset: Open Images v4
- Input size: 320x320
- Does not require a labels file

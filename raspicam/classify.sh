#!/bin/bash
./classify_capture.py \
    --model ../coral/models/mobilenet_v2_1.0_224_quant_edgetpu.tflite \
    --labels ../coral/labels/imagenet_labels.txt


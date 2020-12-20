#!/bin/bash
python3 detect.py \
    --model ../coral/models/ssd_mobilenet_v2_coco_quant_postprocess_edgetpu.tflite \
    --labels ../coral/labels/coco_labels.txt

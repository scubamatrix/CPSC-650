# [Python quickstart](https://www.tensorflow.org/lite/guide/python)

This folder contains code that is based on the Python quickstart tutorial using TensorFlow Lite with Python for embedded devices based on Linux such as Raspberry Pi and Coral devices with Edge TPU.

```bash
    # Get photo
    curl https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/lite/examples/label_image/testdata/grace_hopper.bmp > ./grace_hopper.bmp

    # Get model
    curl https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_1.0_224.tgz | tar xzv -C .

    # Get labels
    curl https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_1.0_224_frozen.tgz  | tar xzv -C .  mobilenet_v1_1.0_224/labels.txt

    # sort labels
    sort -k 2 -t : labels.txt
    sort -k 2 labels.txt
```

```bash
    # Run the sample
    python3 label_image.py \
        --model_file ../coral/models/mobilenet_v1_1.0_224_quant.tflite \
        --label_file ../coral/labels/imagenet_labels.txt \
        --image ./grace_hopper.bmp
```

# [Python quickstart](https://www.tensorflow.org/lite/guide/python)

```bash
    # Get photo
    curl https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/lite/examples/label_image/testdata/grace_hopper.bmp > ./grace_hopper.bmp

    # Get model
    curl https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_1.0_224.tgz | tar xzv -C .

    # Get labels
    curl https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_1.0_224_frozen.tgz  | tar xzv -C .  mobilenet_v1_1.0_224/labels.txt

    # sort labels
    sort -k 2 -t : labels.txt
    sort -k 2 -t : labels.txt
```

```bash
    # Run the sample
    python3 label_image.py \
        --model_file ./mobilenet_v1_1.0_224.tflite \
        --label_file ./mobilenet_v1_1.0_224/labels.txt \
        --image ./grace_hopper.bmp

    # Run the sample
    python3 label_image.py \
        --model_file ./models/mobilenet_v1_1.0_224.tflite \
        --label_file ./labels/mobilenet_v1_1.0_224_labels.txt \
        --image ./penny-and-me.jpg
```

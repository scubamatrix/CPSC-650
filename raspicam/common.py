"""
common.py
Common utilities.
"""
import numpy as np
import tflite_runtime.interpreter as tflite

EDGETPU_SHARED_LIB = "libedgetpu.so.1"


def make_interpreter(model_file):
    model_file, *device = model_file.split("@")
    return tflite.Interpreter(
        model_path=model_file,
        experimental_delegates=[
            tflite.load_delegate(
                EDGETPU_SHARED_LIB, {"device": device[0]} if device else {}
            )
        ],
    )


def input_image_size(interpreter):
    """Returns input image size as (width, height, channels) tuple."""
    _, height, width, channels = interpreter.get_input_details()[0]["shape"]
    return width, height, channels


def input_tensor(interpreter):
    """Returns input tensor view as numpy array of shape (height, width, 3)."""
    tensor_index = interpreter.get_input_details()[0]["index"]
    return interpreter.tensor(tensor_index)()[0]


def output_tensor(interpreter, i):
    """Returns dequantized output tensor if quantized before."""
    output_details = interpreter.get_output_details()[i]
    output_data = np.squeeze(interpreter.tensor(output_details["index"])())
    if "quantization" not in output_details:
        return output_data
    scale, zero_point = output_details["quantization"]
    if scale == 0:
        return output_data - zero_point
    return scale * (output_data - zero_point)

INPUT_SCHEMA = {
    "image_url": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["https://raw.githubusercontent.com/rbgo404/Files/main/dog.jpg"]
    },
    "input_points": {
        'datatype': 'FP32',  # Assuming coordinates are integers
        'required': True,
        'shape': [2],  # Specifies that exactly two integers are expected
        'example': [[426,284]]  # Provides an example as a nested list, consistent with your shape requirement
    }
    
}

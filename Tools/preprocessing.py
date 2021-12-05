import numpy as np

def preprocess_observation(observation):

    # Slice Top Off
    img = observation[34:250:2, ::2]

    # Grey Scale
    img = img.mean(axis=2)
    img = (img - 128).astype(np.int8)

    return img.reshape(108, 80, 1)
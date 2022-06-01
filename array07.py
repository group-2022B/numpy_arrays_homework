import numpy as np


def main():
    """
    Create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.

    """
    return np.array([
        [1, 0, 0, 0, 0],
        [0, 2, 0, 0, 0],
        [0, 0, 3, 0, 0],
        [0, 0, 0, 4, 0],
        [0, 0, 0, 0, 5]
    ])

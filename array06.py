import numpy as np


def main():
    """
    Create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.

    """
    array = np.ones((10, 10))
    array[1:-1, 1:-1] = 0
    # array = np.array([
    #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # ])
    return array
print(main())

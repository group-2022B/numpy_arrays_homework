import numpy as np

def main():
    """
    Create a 3x1 matrix with values from 1 to 3.

    """
    array = []
    item = 1
    for i in range(3):
        rows = []
        for j in range(1):
            rows.append(item)
            item += 1
        array.append(rows)

    return np.array(array)
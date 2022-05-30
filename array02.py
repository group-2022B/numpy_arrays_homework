import numpy as np

def main():
    """
    Create a 3x3 matrix with values from 2 to 10.
    """
    array = []
    item = 2
    for i in range(3):
        rows = []
        for j in range(3):
            rows.append(item)
            item += 1
        array.append(rows)

    return np.array(array)
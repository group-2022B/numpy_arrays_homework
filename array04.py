import numpy as np

def main():
    """
    Create a 3x4 matrix filled with values from 10 to 21.

    """
    array = []
    item = 10
    for i in range(3):
        rows = []
        for j in range(4):
            rows.append(item)
            item += 1
        array.append(rows)

    return np.array(array)

print(main())
import numpy as np

def main():
    """
    Create a 3x8 array filled with zeros values.

    """
    diagonal = 1
    array = []
    for i in range(3):
        rows = []
        for j in range(8):
            rows.append(0)
        array.append(rows)

    return np.array(array, dtype=np.uint8)

print(main())
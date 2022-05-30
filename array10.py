import numpy as np

def main():
    """
    Create a 3x8 array filled with zeros values.

    """
    diagonal = 1
    array = []
    for i in range(7):
        rows = []
        for j in range(12):
            rows.append(1)
        array.append(rows)

    return np.array(array, dtype=np.uint8)

print(main())
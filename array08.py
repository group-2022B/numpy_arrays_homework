import numpy as np

def main():
    """
    Create a 5x2 array filled with ones values.

    """
    diagonal = 1
    array = []
    for i in range(5):
        rows = []
        for j in range(2):
            rows.append(1)
        array.append(rows)

    return np.array(array, dtype=np.uint8)

print(main())
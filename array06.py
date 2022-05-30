import numpy as np

def main():
    """
    Create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.

    """
    array = []
    for i in range(10):
        rows = []
        for j in range(10):
            if i == 0 or i == 9 or j == 0 or j == 9:
                rows.append(1)
            else:
                rows.append(0)
        array.append(rows)

    return np.array(array, dtype=np.uint8)
# x = np.ones(shape=(10,10), dtype=np.uint8)
# x[1:-1,1:-1] = 0
# print(x)
# print(main())
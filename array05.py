import numpy as np

def main():
    """
    Create a 8x8 identity matrix, i.e. diagonal elements are 1, the rest are 0.

    """
    array = []
    for i in range(8):
        rows = []
        for j in range(8):
            if i == j:
                rows.append(1)
            else:
                rows.append(0)
        array.append(rows)

    return np.array(array)
print(np.eye(8,8,dtype=int))
print(main())
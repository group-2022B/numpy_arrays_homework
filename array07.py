import numpy as np

def main():
    """
    Create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.

    """
    diagonal = 1
    array = []
    for i in range(5):
        rows = []
        for j in range(5):
            if i == j:
                rows.append(diagonal)
                diagonal += 1
            else:
                rows.append(0)
        array.append(rows)

    return np.array(array, dtype=np.uint8)
# x = np.ones(shape=(10,10), dtype=np.uint8)
# x[1:-1,1:-1] = 0
# print(x)
print(main())
excepted = np.array([[1, 0, 0, 0, 0],[0, 2, 0, 0, 0],[0, 0, 3, 0, 0],[0, 0, 0, 4, 0],[0, 0, 0, 0, 5]])
print(excepted)
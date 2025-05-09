import numpy as np

# 2D array
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
# 1D array
array_1d = np.array([10, 20, 30])
# broadcasting addition
result = array_2d + array_1d

print("2D array:\n", array_2d)
print("1D array:\n", array_1d)
print("result of broadcasting addition:\n", result)

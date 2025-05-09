import numpy as np

# Two 1D arrays
array_a = np.array([1, 2, 3, 4, 5])
array_b = np.array([10, 20, 30, 40, 50])

# Vectorized element-wise multiplication
result = array_a * array_b

print("Array A:\n", array_a)
print("Array B:\n", array_b)
print("Result of Vectorized Multiplication:\n", result)

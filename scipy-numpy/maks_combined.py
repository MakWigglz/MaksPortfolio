import numpy as np

# 2D array
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# Two 1D arrays
array_add = np.array([10, 20, 30])
array_mult = np.array([1, 2, 3])

# Broadcasting addition
broadcasted_result = array_2d + array_add

# Vectorized multiplication
final_result = broadcasted_result * array_mult[:, np.newaxis]

print("2D Array:\n", array_2d)
print("1D Array for Addition:\n", array_add)
print("1D Array for Multiplication:\n", array_mult)
print("Result of Combined Broadcasting and Vectorization:\n", final_result)

"""
    (new-matplot-venv) amakki@As-MacBook-Pro numpy % python3 maks_vectorization.py
Array A:
 [1 2 3 4 5]
Array B:
 [10 20 30 40 50]
Result of Vectorized Multiplication:
 [ 10  40  90 160 250]
(new-matplot-venv) amakki@As-MacBook-Pro numpy % python3 maks_combined.py
2D Array:
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
1D Array for Addition:
 [10 20 30]
1D Array for Multiplication:
 [1 2 3]
Result of Combined Broadcasting and Vectorization:
 [[ 11  22  33]
 [ 28  50  72]
 [ 51  84 117]]
(new-matplot-venv) amakki@As-MacBook-Pro numpy % 
"""

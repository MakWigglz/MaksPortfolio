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

"""
Last login: Fri May  9 20:06:47 on ttys004
(base) amakki@As-MacBook-Pro ~ % cd /Users/amakki/Documents/Coding-Design/GitHub/Maksportfolio/data_structures_analysis/numpy
(base) amakki@As-MacBook-Pro numpy % conda activate new-matplot-venv
(new-matplot-venv) amakki@As-MacBook-Pro numpy % python3 maks_broadcasting.py
2D Array:
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
1D Array:
 [10 20 30]
Result of Broadcasting Addition:
 [[11 22 33]
 [14 25 36]
 [17 28 39]]
(new-matplot-v
    """

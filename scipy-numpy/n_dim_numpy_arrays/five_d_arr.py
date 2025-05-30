import numpy as np

five_d_array = np.array([
    # First 4D Block (index 0)
    [
        # First 3D Plane within Block 0 (index 0,0)
        [
            # First 2D Matrix within Plane 0,0 (index 0,0,0)
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [33, 34, 35, 36]
            ]
        ],
        # Second 3D Plane within Block 0 (index 0,1)
        [
            # First 2D Matrix within Plane 0,1 (index 0,1,0)
            [
                [9, 10, 11, 12],
                [13, 14, 15, 16],
                [37, 38, 39, 40]
            ]
        ]
    ],
    # Second 4D Block (index 1)
    [
        # First 3D Plane within Block 1 (index 1,0)
        [
            # First 2D Matrix within Plane 1,0 (index 1,0,0)
            [
                [17, 18, 19, 20],
                [21, 22, 23, 24],
                [41, 42, 43, 44]
            ]
        ],
        # Second 3D Plane within Block 1 (index 1,1)
        [
            # First 2D Matrix within Plane 1,1 (index 1,1,0)
            [
                [25, 26, 27, 28],
                [29, 30, 31, 32],
                [45, 46, 47, 48]
            ]
        ]
    ],
    # Third 4D Block (index 2)
    [
        # First 3D Plane within Block 2 (index 2,0)
        [
            # First 2D Matrix within Plane 2,0 (index 2,0,0)
            [
                [49, 50, 51, 52],
                [53, 54, 55, 56],
                [57, 58, 59, 60]
            ]
        ],
        # Second 3D Plane within Block 2 (index 2,1)
        [
            # First 2D Matrix within Plane 2,1 (index 2,1,0)
            [
                [61, 62, 63, 64],
                [65, 66, 67, 68],
                [69, 70, 71, 72]
            ]
        ]
    ]
])

print("--- The Constructed NumPy Array ---")
print(five_d_array)
print("\n--- Array Properties ---")
print(f"Shape: {five_d_array.shape}")
print(f"Number of dimensions (ndim): {five_d_array.ndim}")

"""
-------------------------------------------------------
t06.py
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-05-11"
-------------------------------------------------------
"""
# Imports
from functions import matrix_rotate_right

# Constants

test_cases = [
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
        ([[1, 2, 3], [4, 5, 6]], [[4, 1], [5, 2], [6, 3]]),
        ([[1]], [[1]]),
        ([], [])
    ]
for matrix, expected in test_cases:
    result = matrix_rotate_right(matrix)
    assert result == expected, f"Test failed for matrix {matrix}. Expected {expected}, got {result}"
    print(f"Test passed for matrix {matrix}. Rotated Right: {result}")


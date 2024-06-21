"""
-------------------------------------------------------
t04.py
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-05-11"
-------------------------------------------------------
"""
# Imports
from functions import matrix_transpose

# Constants

test_cases = [
        ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),  # 2x3 matrix
        ([[1, 2], [3, 4], [5, 6]], [[1, 3, 5], [2, 4, 6]]),  # 3x2 matrix
        ([[1]], [[1]]),                                      # 1x1 matrix
        ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),                # 2x2 square matrix
        ([], [])                                             # Empty matrix
    ]

for matrix, expected in test_cases:
    result = matrix_transpose(matrix)
    print(f'{matrix} -> {result} (expected {expected})')
    assert result == expected
    print('All tests passed')




"""
-------------------------------------------------------
t05
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-05-11"
-------------------------------------------------------
"""
# Imports
from functions import matrix_flatten

# Constants

test_cases = [
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([[1], [2], [3]], [1, 2, 3]),
        ([[]], []),
        ([[], []], []),
        ([[1, 2, 3]], [1, 2, 3])
    ]

for matrix, expected in test_cases:
    result = matrix_flatten(matrix)
    print(f'{matrix} -> {result} (expected {expected})')
    assert result == expected
    print('All tests passed')

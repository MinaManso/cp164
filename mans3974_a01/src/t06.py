"""
-------------------------------------------------------
t06
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-05-11"
-------------------------------------------------------
"""
# Imports
from functions import matrixes_multiply

# Constants

test_cases = [
        ([[1, 2], [3, 4]], [[2, 0], [1, 2]], [[4, 4], [10, 8]]),
        ([[1, 2, 3]], [[1], [2], [3]], [[14]]),
        ([[1, 0], [0, 1]], [[4, 1], [2, 2]], [[4, 1], [2, 2]]),
        ([], [], [])
    ]
for a, b, expected in test_cases:
    result = matrixes_multiply(a, b)
    assert result == expected, f"Test failed. Expected {expected}, got {result}"
    print(f"Test passed. Multiplied: {result}")

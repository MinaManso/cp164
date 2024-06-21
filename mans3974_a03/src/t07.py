"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-05-26"
-------------------------------------------------------
"""
# Imports

# Constants
from functions import is_mirror_stack

test_string = "abcba"
valid_chars = "abc"
pivot = "b"
result = is_mirror_stack(test_string, valid_chars, pivot)
print(f"Result of mirror check for '{test_string}' is {result}")
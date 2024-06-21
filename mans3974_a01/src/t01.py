"""
-------------------------------------------------------
t01
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-05-11"
-------------------------------------------------------
"""
# Imports
from functions import list_subtraction


# Constants
list1 = [1,2,3,4,5,]
list2 = [2,4]

list_subtraction(list1, list2)
assert list1 == [1, 3, 5], f"Test 1 failed: {list1}"


print("All tests passed!")



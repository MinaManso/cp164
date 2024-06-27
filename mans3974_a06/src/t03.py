"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-06-23"
-------------------------------------------------------
"""
# Imports

# Constants

# Assuming Deque class is imported from deque_linked module
from Deque_linked import Deque

def test_deque():
    d = Deque()
    print("Test isEmpty (True expected):", d.is_empty())

    d.insert_rear(1)
    d.insert_front(0)
    d.insert_rear(2)
    print("Test Peek Front (0 expected):", d.peek_front())
    print("Test Peek Rear (2 expected):", d.peek_rear())

    print("Test Remove Front (0 expected):", d.remove_front())
    print("Test Remove Rear (2 expected):", d.remove_rear())
    print("Test isEmpty (False expected):", d.is_empty())

    d.remove_front()
    print("Test isEmpty (True expected):", d.is_empty())

# Run the test
test_deque()

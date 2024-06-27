"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-06-22"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue

def test_queue():
    q = Queue()
    print("Test isEmpty (True expected):", q.is_empty())

    q.insert(1)
    q.insert(2)
    q.insert(3)
    print("Test Peek (1 expected):", q.peek())

    print("Test Remove (1 expected):", q.remove())
    print("Test Remove (2 expected):", q.remove())
    print("Test isEmpty (False expected):", q.is_empty())

    q.remove()
    print("Test isEmpty (True expected):", q.is_empty())
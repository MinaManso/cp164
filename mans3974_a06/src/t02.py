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

# Assuming Priority_Queue class is imported from priority_queue_linked module
from Priority_Queue_linked import Priority_Queue

def test_priority_queue():
    pq = Priority_Queue()
    print("Test isEmpty (True expected):", pq.is_empty())

    pq.insert(3)
    pq.insert(1)
    pq.insert(2)
    print("Test Peek (1 expected):", pq.peek())  # Assuming lower values have higher priority

    print("Test Remove (1 expected):", pq.remove())
    print("Test Remove (2 expected):", pq.remove())
    print("Test isEmpty (False expected):", pq.is_empty())

    pq.remove()
    print("Test isEmpty (True expected):", pq.is_empty())

# Run the test
test_priority_queue()

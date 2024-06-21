"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-06-01"
-------------------------------------------------------
"""
# Imports

# Constants

from Queue_array import Queue  # Adjust the import statement based on your file structure

def test_queue_eq():
    print("Testing __eq__ method...\n")

    # Create two identical queues
    q1 = Queue()
    q2 = Queue()
    for i in range(1, 6):
        q1.insert(i)
        q2.insert(i)

    # Create a queue with different elements
    q3 = Queue()
    for i in range(1, 6):
        q3.insert(i + 1)

    # Create an empty queue
    q4 = Queue()

    # Create another empty queue
    q5 = Queue()

    # Test equality of two identical queues
    print("Comparing two identical queues (q1 and q2):", q1 == q2)  # Should be True

    # Test equality of two different queues
    print("Comparing two different queues (q1 and q3):", q1 == q3)  # Should be False

    # Test equality of a queue and an empty queue
    print("Comparing a non-empty queue (q1) and an empty queue (q4):", q1 == q4)  # Should be False

    # Test equality of two empty queues
    print("Comparing two empty queues (q4 and q5):", q4 == q5)  # Should be True

    # Test equality of two queues with different capacities but same elements
    q6 = Queue(20)
    for i in range(1, 6):
        q6.insert(i)
    print("Comparing two queues with different capacities (q1 and q6):", q1 == q6)  # Should be True

    print("\n__eq__ method tests completed.")
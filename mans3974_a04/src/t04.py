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

from Queue_circular import Queue
from functions import queue_combine


def test_queue_combine():
    print("Testing queue_combine function...\n")

    # Create two source queues
    source1 = Queue()
    source2 = Queue()

    for i in range(1, 6):
        source1.insert(i)

    for i in range(6, 11):
        source2.insert(i)

    # Combine the queues
    target = queue_combine(source1, source2)

    # Check the target queue
    print("Target queue after combining:")
    print(list(target))

    # Check if source queues are empty
    print("\nSource queues after combining:")
    print("source1 is empty:", source1.is_empty())
    print("source2 is empty:", source2.is_empty())

    print("\nqueue_combine function tests completed.")

if __name__ == "__main__":
    test_queue_combine()

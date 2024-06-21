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

from Queue_circular import Queue   # Adjust the import statement based on your file structure
from functions import pq_split_key  # Adjust the import statement based on your file structure

def test_pq_split_key():
    print("Testing pq_split_key function...\n")

    # Create a source priority queue
    source = Queue()

    values = [5, 1, 9, 3, 7, 4, 6]
    for value in values:
        source.insert(value)

    key = 4

    # Split the queue
    target1, target2 = pq_split_key(source, key)

    # Check the target queues
    print("Target1 queue (higher priority than key):")
    print(list(target1))

    print("\nTarget2 queue (lower or equal priority to key):")
    print(list(target2))

    # Check if source queue is empty
    print("\nSource queue after splitting:")
    print("source is empty:", source.is_empty())

    print("\npq_split_key function tests completed.")

if __name__ == "__main__":
    test_pq_split_key()

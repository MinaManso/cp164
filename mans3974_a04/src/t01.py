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


def test_queue():
    print("Testing Queue class...\n")

    # Create a queue with default capacity
    q1 = Queue()
    print("Empty queue created with default capacity:")
    print("is_empty:", q1.is_empty())
    print("is_full:", q1.is_full())
    print("Length:", len(q1))

    # Insert elements into the queue
    print("\nInserting elements 1 to 5 into the queue...")
    for i in range(1, 6):
        q1.insert(i)
        print(f"Inserted {i}, is_full: {q1.is_full()}, Length: {len(q1)}")

    # Peek at the front element
    print("\nPeeking at the front element:", q1.peek())

    # Remove elements from the queue
    print("\nRemoving elements from the queue...")
    while not q1.is_empty():
        print("Removed:", q1.remove(), "Remaining Length:", len(q1))

    # Test is_empty after removals
    print("\nQueue after all removals:")
    print("is_empty:", q1.is_empty())
    print("is_full:", q1.is_full())

    # Test equality of two queues
    q2 = Queue()
    for i in range(1, 6):
        q2.insert(i)

    q3 = Queue()
    for i in range(1, 6):
        q3.insert(i)

    q4 = Queue()
    for i in range(1, 6):
        q4.insert(i + 1)

    print("\nComparing two identical queues (q2 and q3):", q2 == q3)
    print("Comparing two different queues (q2 and q4):", q2 == q4)

    # Test iterator
    print("\nTesting iterator...")
    q5 = Queue()
    for i in range(1, 6):
        q5.insert(i)
    print("Queue elements using iterator:", list(q5))

    print("\nAll tests completed.")



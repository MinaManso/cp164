#
from List_array import List
def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        stack.push(source.pop())
    
    return
    


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():
        target.insert(0, stack.pop())
    
    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    test_cases = [
        ([11, 22, 33, 44], [44, 33, 22, 11]),
        ([55, 44, 33, 22, 11], [11, 22, 33, 44, 55]),
        ([22, 33, 11, 55, 44], [44, 55, 11, 33, 22])
    ]

    for source, expected in test_cases:
        stack = Stack()  # Reset stack for each test case
        array_to_stack(stack, source.copy())  # Use a copy to keep source intact for assert
        result = stack.items
        assert result == expected, f"Test failed for source {source}. Expected {expected}, got {result}"
        print(f"Test passed for source {source}. Stack after operation: {result}")
    
    
    s = Stack()
    for i in source:
        s.push(i)
    
    print("Stack: ", s)
    print("Is empty: ", s.is_empty())
    print("Peek: ", s.peek())
    print("Pop: ", s.pop())

    return
    



def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        pq.insert(source.pop(0))
    return

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())
    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    print("Testing Priority Queue with data:", a)

    # Test is_empty on empty priority queue
    print("Is empty:", pq.is_empty())

    # Test insert and peek
    for value in a:
        pq.insert(value)
        print(f"Inserted {value}, Peek: {pq.peek()}")

    # Test is_empty on non-empty priority queue
    print("Is empty after inserts:", pq.is_empty())

    # Test remove
    while not pq.is_empty():
        value = pq.remove()
        print(f"Removed {value}, New Peek: {pq.peek() if not pq.is_empty() else 'None'}")

    # Test is_empty after removing all elements
    print("Is empty after removals:", pq.is_empty())

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand

    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        llist.append(source.pop(0))
        

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(llist) > 0:
        target.append(llist.pop(0))
    
    
def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    # Test is_empty on an empty list
    print("Test is_empty on empty list:", lst.is_empty())

    # Test append and __len__
    for value in source:
        lst.append(value)
    print("List after appending values:", list(lst))
    print("Length of list after appending values:", len(lst))

    # Test __getitem__
    for i in range(len(lst)):
        print(f"Element at index {i}:", lst[i])

    # Test __setitem__
    lst[0] = source[-1]
    print("List after setting first element to last value in source:", list(lst))

    # Test __contains__
    key = source[1]
    print(f"List contains {key}:", key in lst)

    # Test find
    print(f"Find value {key} in list:", lst.find(key))

    # Test index
    print(f"Index of value {key} in list:", lst.index(key))

    # Test max and min
    print("Maximum value in list:", lst.max())
    print("Minimum value in list:", lst.min())

    # Test count
    print(f"Count of value {key} in list:", lst.count(key))

    # Test remove
    print(f"Remove value {key} from list:", lst.remove(key))
    print("List after removing value:", list(lst))

    # Test pop
    print("Pop last value from list:", lst.pop())
    print("List after popping last value:", list(lst))
    
    # Test prepend
    lst.prepend(source[0])
    print("List after prepending value:", list(lst))

    # Test peek
    print("Peek first value in list:", lst.peek())

    # Test reverse
    lst.reverse()
    print("List after reversing:", list(lst))

    # Test copy
    copied_lst = lst.copy()
    print("Copied list:", list(copied_lst))

    # Test clean
    lst.append(source[1])
    lst.append(source[1])
    print("List before cleaning duplicates:", list(lst))
    lst.clean()
    print("List after cleaning duplicates:", list(lst))

    # Test split
    lst1, lst2 = lst.split()
    print("List after splitting into two lists:")
    print("First half:", list(lst1))
    print("Second half:", list(lst2))

    # Test split_alt
    lst.combine(lst1, lst2)
    lst1, lst2 = lst.split_alt()
    print("List after alternate splitting:")
    print("First alternate list:", list(lst1))
    print("Second alternate list:", list(lst2))

    # Test split_apply
    def is_even(n):
        return n % 2 == 0

    lst.combine(lst1, lst2)
    lst1, lst2 = lst.split_apply(is_even)
    print("List after splitting with function:")
    print("List with even values:", list(lst1))
    print("List with odd values:", list(lst2))

    # Test split_key
    key = source[2]
    lst.combine(lst1, lst2)
    lst1, lst2 = lst.split_key(key)
    print("List after splitting by key:")
    print(f"List with values < {key}:", list(lst1))
    print(f"List with values >= {key}:", list(lst2))

    # Test union
    lst.union(lst1, lst2)
    print("List after union of two lists:", list(lst))

    # Test apply
    def square(n):
        return n * n

    lst.apply(square)
    print("List after applying square function:", list(lst))
    # Test insert
    insert_index = 1
    insert_value = source[0]
    lst.insert(insert_index, insert_value)
    print(f"List after inserting {insert_value} at index {insert_index}:", list(lst))

    return
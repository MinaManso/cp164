"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-06-09"
-------------------------------------------------------
"""
# Imports
from List_array import List

def test_list():
    # Create a List object
    lst = List()

    # Test append
    lst.append(5)
    lst.append(3)
    lst.append(9)
    lst.append(1)
    assert list(lst) == [5, 3, 9, 1], "Append method failed"

    # Test length
    assert len(lst) == 4, "Length method failed"

    # Test __contains__
    assert 3 in lst, "__contains__ method failed"
    assert 7 not in lst, "__contains__ method failed"

    # Test __getitem__
    assert lst[0] == 5, "__getitem__ method failed"
    assert lst[2] == 9, "__getitem__ method failed"

    # Test __setitem__
    lst[1] = 7
    assert lst[1] == 7, "__setitem__ method failed"

    # Test insert
    lst.insert(2, 8)
    assert list(lst) == [5, 7, 8, 9, 1], "Insert method failed"
    lst.insert(0, 0)
    assert list(lst) == [0, 5, 7, 8, 9, 1], "Insert method failed"

    # Test count
    lst.append(5)
    assert lst.count(5) == 2, "Count method failed"

    # Test find
    assert lst.find(8) == 8, "Find method failed"
    assert lst.find(10) == None, "Find method failed"

    # Test max
    assert lst.max() == 9, "Max method failed"

    # Test min
    assert lst.min() == 0, "Min method failed"

    # Test remove
    assert lst.remove(8) == 8, "Remove method failed"
    assert lst.remove(10) == None, "Remove method failed"

    # Test pop
    assert lst.pop() == 5, "Pop method failed"
    assert lst.pop(0) == 0, "Pop method failed"

    # Test is_empty
    assert lst.is_empty() == False, "Is_empty method failed"
    lst.pop()
    lst.pop()
    lst.pop()
    lst.pop()
    assert lst.is_empty() == True, "Is_empty method failed"

    # Test combine
    s1 = List()
    s2 = List()
    s1.append(1)
    s1.append(3)
    s1.append(5)
    s2.append(2)
    s2.append(4)
    s2.append(6)
    lst.combine(s1, s2)
    assert list(lst) == [1, 2, 3, 4, 5, 6], "Combine method failed"
    assert list(s1) == [], "Combine method failed - Source1 not empty"
    assert list(s2) == [], "Combine method failed - Source2 not empty"

    # Test split
    lst.append(7)
    lst.append(8)
    t1, t2 = lst.split()
    assert list(t1) == [1, 2, 3, 4], "Split method failed"
    assert list(t2) == [5, 6, 7, 8], "Split method failed"

    # Test split_alt
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(4)
    lst.append(5)
    t1, t2 = lst.split_alt()
    assert list(t1) == [1, 3, 5], "Split_alt method failed"
    assert list(t2) == [2, 4], "Split_alt method failed"

    # Test clean
    lst.append(1)
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.clean()
    assert list(lst) == [1, 2, 3], "Clean method failed"

    # Test intersection
    s1 = List()
    s2 = List()
    s1.append(1)
    s1.append(2)
    s2.append(2)
    s2.append(3)
    lst.intersection(s1, s2)
    assert list(lst) == [2], "Intersection method failed"

    # Test union
    lst.union(s1, s2)
    assert list(lst) == [1, 2, 3], "Union method failed"

    print("All tests passed!")

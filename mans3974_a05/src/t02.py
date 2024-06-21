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

# Constants

from Sorted_list_array import Sorted_List

def test_sorted_list():
    # Create a Sorted_List object
    sl = Sorted_List()
    
    # Test insertion
    sl.insert(5)
    sl.insert(3)
    sl.insert(9)
    sl.insert(1)
    assert list(sl) == [1, 3, 5, 9], "Insert method failed"
    
    # Test length
    assert len(sl) == 4, "Length method failed"
    
    # Test __contains__
    assert 3 in sl, "__contains__ method failed"
    assert 7 not in sl, "__contains__ method failed"
    
    # Test __getitem__
    assert sl[0] == 1, "__getitem__ method failed"
    assert sl[2] == 5, "__getitem__ method failed"
    
    # Test find
    assert sl.find(3) == 3, "Find method failed"
    assert sl.find(7) == None, "Find method failed"
    
    # Test count
    sl.insert(3)
    assert sl.count(3) == 2, "Count method failed"
    
    # Test max
    assert sl.max() == 9, "Max method failed"
    
    # Test min
    assert sl.min() == 1, "Min method failed"
    
    # Test remove
    assert sl.remove(3) == 3, "Remove method failed"
    assert sl.remove(7) == None, "Remove method failed"
    assert list(sl) == [1, 3, 5, 9], "Remove method failed"
    
    # Test pop
    assert sl.pop() == 9, "Pop method failed"
    assert sl.pop(0) == 1, "Pop method failed"
    assert list(sl) == [3, 5], "Pop method failed"
    
    # Test is_empty
    assert sl.is_empty() == False, "Is_empty method failed"
    sl.pop()
    sl.pop()
    assert sl.is_empty() == True, "Is_empty method failed"
    
    # Test split
    sl.insert(1)
    sl.insert(2)
    sl.insert(3)
    sl.insert(4)
    sl.insert(5)
    t1, t2 = sl.split()
    assert list(t1) == [1, 2], "Split method failed"
    assert list(t2) == [3, 4, 5], "Split method failed"
    
    # Test split_alt
    sl.insert(1)
    sl.insert(2)
    sl.insert(3)
    sl.insert(4)
    sl.insert(5)
    t1, t2 = sl.split_alt()
    assert list(t1) == [1, 3, 5], "Split_alt method failed"
    assert list(t2) == [2, 4], "Split_alt method failed"
    
    # Test clean
    sl.insert(1)
    sl.insert(1)
    sl.insert(2)
    sl.insert(3)
    sl.clean()
    assert list(sl) == [1, 2, 3], "Clean method failed"
    
    # Test intersection
    s1 = Sorted_List()
    s2 = Sorted_List()
    s1.insert(1)
    s1.insert(2)
    s2.insert(2)
    s2.insert(3)
    sl.intersection(s1, s2)
    assert list(sl) == [2], "Intersection method failed"
    
    # Test union
    sl.union(s1, s2)
    assert list(sl) == [1, 2, 3], "Union method failed"
    
    # Test combine
    def test_sorted_list():
    # Create a Sorted_List object
        sl = Sorted_List()
    
    # Other tests...
    
    # Test combine
    s1 = Sorted_List()
    s2 = Sorted_List()
    s1.insert(1)
    s1.insert(3)
    s1.insert(5)
    s2.insert(2)
    s2.insert(4)
    s2.insert(6)
    
    sl.combine(s1, s2)
    assert list(sl) == [1, 2, 3, 4, 5, 6], "Combine method failed"
    assert list(s1) == [], "Combine method failed - Source1 not empty"
    assert list(s2) == [], "Combine method failed - Source2 not empty"
    
    print("All tests passed!")
    
    print("All tests passed!")

if __name__ == "__main__":
    test_sorted_list()

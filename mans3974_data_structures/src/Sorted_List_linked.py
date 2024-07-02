"""
-------------------------------------------------------
Linked version of the Sorted_List ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-06-10"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _SL_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SL_Node(value, next_)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            next_ - another sorted list node (_SL_Node)
        Returns:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
        return


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: sl = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = sl.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """

        # your code here

        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Returns:
            Returns the number of values in the list.
        -------------------------------------------------------
        """

        # your code here

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        new_node = _SL_Node(deepcopy(value), None)

        if self._front is None or self._front._value >= value:
            # Insert at front
            new_node._next = self._front
            self._front = new_node
            if self._rear is None:
                self._rear = new_node
            
        else:
            current = self._front
            while current._next is not None and current._next._value < value:
                current = current._next
            new_node._next = current._next
            current._next = new_node
            if current._next._next is None:
                self._rear = new_node
        self._count += 1
        # your code here

        return

    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure. 
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_SL_Node)
            current - pointer to the node containing key (_SL_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        index = 0

        while current is not None and current._value < key:
            previous = current
            current = current._next
            index += 1

        if current is not None and current._value != key:
            return None, None, -1
        
        return previous, current, index

        # your code here

        

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        found = False
        value = None

        # Artificially limit the loop to the maximum possible size of the list
        for _ in range(self._count):
            if current is None:
                break
            if current._value == key:
                found = True
                value = current._value
                break
            previous = current
            current = current._next

        if found:
            if previous is None:
                # Removing the first node
                self._front = self._front._next
                if self._front is None:
                    # List had one element, now empty
                    self._rear = None
            else:
                # Removing any other node
                previous._next = current._next
                if previous._next is None:
                    # Adjust rear if needed
                    self._rear = previous
            self._count -= 1

        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        value = self._front._value
        self._front = self._front._next

        if self._front is None:
            self._rear = None
        
        self._count -= 1

        # your code here

        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            All values matching key are removed from the list.
        -------------------------------------------------------
        """
        previous = None
        current = self._front

        while current is not None:
            next_node = current._next
            if current._value == key:
                if previous is None:
                    self._front = next_node
                    if self._front is None:
                        self._rear = None
                else:
                    previous._next = next_node
                    if next_node is None:
                        self._rear = previous
                self._count -= 1

            else:
                previous = current
            current = next_node

        # your code here

        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        _, current, _ = self._linear_search(key)


        # your code here

        return deepcopy(current._value) if current else None

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"


        # your code here

        return deepcopy(self._front._value)

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """
        _, _, index = self._linear_search(key)

        # your code here

        return index

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """

        # your code here

        return -self._count <= i < self._count

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        current = self._front
        if i < 0:
            i += self._count
        
        for _ in range(i):
            current = current._next

        # your code here

        return deepcopy(current._value)

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """

        _, current, _ = self._linear_search(key)

        # your code here

        return current is not None

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        # your code here

        return deepcopy(self._rear._value)

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find minimum of an empty list"

        # your code here

        return deepcopy(self._front._value)

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in the sorted list (int)
        -------------------------------------------------------
        """

        count = 0
        current = self._front
        while current is not None:
            if current._value == key:
                count += 1
            current = current._next
        return count

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        if self._front is not None:
            seen = set()
            previous = None
            current = self._front
            while current is not None:
                if current._value in seen:
                    # If the value has already been seen, remove the current node
                    if previous is not None:
                        previous._next = current._next
                    else:
                        self._front = current._next  # Update the front if it's the first element
                    if current._next is None:
                        self._rear = previous  # Update the rear if the last element was removed
                    self._count -= 1  # Decrement the count for each removal
                else:
                    # If it's a new value, add to seen and move previous pointer
                    seen.add(current._value)
                    previous = current
                current = current._next
            if previous:
                previous._next = None

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:
            i = args[0]

            if i < 0:
                # index is negative
                i = self._count + i
            j = 0

            while j < i:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value

        if previous is None:
            # Update the front
            self._front = current._next
        else:
            # Update any other node
            previous._next = current._next
        self._count -= 1
        return value

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        current1 = source1._front
        while current1:
            current2 = source2._front
            while current2:
                if current1._value == current2._value and not self.__contains__(current1._value):
                    self.insert(current1._value)
                current2 = current2._next
            current1 = current1._next

        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        current = source1._front
        while current:
            if not self.__contains__(current._value):
                self.insert(current._value)
            current = current._next

        current = source2._front
        while current:
            if not self.__contains__(current._value):
                self.insert(current._value)
            current = current._next

        return

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        slow = self._front
        fast = self._front
        if fast:
            fast = fast._next
        while fast and fast._next:
            slow = slow._next
            fast = fast._next._next

        target1 = Sorted_List()
        target2 = Sorted_List()
        current = self._front
        while current != slow._next:
            target1.insert(current._value)
            current = current._next

        current = slow._next
        while current:
            target2.insert(current._value)
            current = current._next

        self._front = self._rear = None
        self._count = 0
        return target1, target2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key. At finish self is empty.
        Use: target1, target2 = lst.split_key()
        -------------------------------------------------------
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """

        target1 = Sorted_List()
        target2 = Sorted_List()
        current = self._front
        while current:
            if current._value <= key:
                target1.insert(current._value)
            else:
                target2.insert(current._value)
            current = current._next
        self._front = self._rear = None
        self._count = 0
        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements. At finish
        self is empty. Order of even and odd is not significant.
        (iterative version)
        Use: even, odd = l.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even indexed elements of the list (Sorted_List)
            odd - the odd indexed elements of the list (Sorted_List)
                The List is empty.
        -------------------------------------------------------
        """

        even = Sorted_List()
        odd = Sorted_List()
        current = self._front
        index = 0
        while current is not None:
            next_node = current._next
            if index % 2 == 0:
                even.insert(current._value)
            else:
                odd.insert(current._value)
            current = next_node
            index += 1
        self._front = self._rear = None
        self._count = 0
        return even, odd

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        
        target1 = Sorted_List()
        target2 = Sorted_List()
        mid = self._count // 2
        current = self._front
        index = 0
        while current is not None:
            next_node = current._next
            if index < mid:
                target1.insert(current._value)
            else:
                target2.insert(current._value)
            current = next_node
            index += 1
        self._front = self._rear = None
        self._count = 0
        return target1, target2

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Sorted_Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a sorted list (Sorted_List)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        if self._count != target._count:
            return False
        current1 = self._front
        current2 = target._front
        while current1 is not None:
            if current1._value != current2._value:
                return False
            current1 = current1._next
            current2 = current2._next
        return True

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = l.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -------------------------------------------------------
        """

        new_list = Sorted_List()
        current = self._front
        while current is not None:
            new_list.insert(current._value)
            current = current._next
        return new_list

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        At finish, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        self._front = None
        self._rear = None
        self._count = 0
        current1 = source1._front
        current2 = source2._front
        last = None

        while current1 is not None or current2 is not None:
            if current1 is not None:
                if self._front is None:
                    self._front = current1
                else:
                    last._next = current1
                last = current1
                current1 = current1._next
                self._count += 1

            if current2 is not None:
                if self._front is None:
                    self._front = current2
                else:
                    last._next = current2
                last = current2
                current2 = current2._next
                self._count += 1

        if last is not None:
            last._next = None
        self._rear = last

        source1._front = None
        source1._rear = None
        source1._count = 0
        source2._front = None
        source2._rear = None
        source2._count = 0

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_SL_Node)
            current - pointer to the node containing key (_SL_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        def _search_recursive(node, prev, idx):
            if node is None:
                return None, None, -1
            
            elif node._value == key:
                return prev, node, idx
            
            else:
                return _search_recursive(node._next, node, idx + 1)
            

        # your code here

        return _search_recursive(self._front, None, 0)

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list.
        Use: sl.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """

        def _clean_recursive(previous, current):
            if current is None:
                return
            if current._next is not None and current._value == current._next._value:
                current._next = current._next._next
                _clean_recursive(previous, current)
            else:
                _clean_recursive(current, current._next)

        _clean_recursive(None, self._front)

    def identical_r(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (recursive version)
        Use: b = l.identical_r(rs)
        -------------------------------------------------------
        Parameters:
            rs - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as rs
                in the same order, otherwise False.
        -------------------------------------------------------
        """

        def _identical_recursive(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is not None and node2 is not None and node1._value == node2._value:
                return _identical_recursive(node1._next, node2._next)
            else:
                return False

        return _identical_recursive(self._front, rs._front)

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        def _intersect_recursive(list1, list2, result=None):
            if list1 is None or list2 is None:
                return result
            elif list1._value == list2._value:
                if result is None or result._value != list1._value:
                    new_node = _SL_Node(list1._value, None)
                    if result is None:
                        result = new_node
                    else:
                        result._next = new_node
                    return _intersect_recursive(list1._next, list2._next, new_node)
                else:
                    return _intersect_recursive(list1._next, list2._next, result)
            elif list1._value < list2._value:
                return _intersect_recursive(list1._next, list2, result)
            else:
                return _intersect_recursive(list1, list2._next, result)

        self._front = _intersect_recursive(source1._front, source2._front)

        return

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = l.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -----------------------------------------------------------
        """

        def _copy_recursive(node):
            if node is None:
                return None
            else:
                new_node = _SL_Node(node._value, _copy_recursive(node._next))
                return new_node

        new_list = Sorted_List()
        new_list._front = _copy_recursive(self._front)
        return new_list

    def combine_r(self, rs):
        """
        -------------------------------------------------------
        Combines contents of two lists into a third.
        Use: new_list = l1.combine(rs)
        -------------------------------------------------------
        Parameters:
            rs- an linked-based List (Sorted_List)
        Returns:
            new_list - the contents of the current Sorted_List and rs
            are interlaced into new_list - current Sorted_List and rs
            are empty (Sorted_List)
        -------------------------------------------------------
        """

        def _combine_recursive(node1, node2):
            if node1 is None:
                return node2
            elif node2 is None:
                return node1
            else:
                node1._next = _combine_recursive(node2, node1._next)
                return node1

        self._front = _combine_recursive(self._front, rs._front)
        rs._front = None  # Empties the rs list

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        def _union_recursive(node1, node2, result=None):
            if node1 is None and node2 is None:
                return result
            elif node1 is not None and (node2 is None or node1._value <= node2._value):
                if result is None or result._value != node1._value:
                    new_node = _SL_Node(node1._value, None)
                    if result is None:
                        result = new_node
                    else:
                        result._next = new_node
                    return _union_recursive(node1._next, node2, new_node)
                else:
                    return _union_recursive(node1._next, node2, result)
            else:
                if result is None or result._value != node2._value:
                    new_node = _SL_Node(node2._value, None)
                    if result is None:
                        result = new_node
                    else:
                        result._next = new_node
                    return _union_recursive(node1, node2._next, new_node)
                else:
                    return _union_recursive(node1, node2._next, result)

        self._front = _union_recursive(source1._front, source2._front)

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list  
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
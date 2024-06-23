"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-06-10"
-------------------------------------------------------
"""
from copy import deepcopy



class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, next_)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        # your code here
        return self._count

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        new_node = _List_Node(deepcopy(value), self._front)

    # Check if the list was empty and update the rear as well
        if self._rear is None:
            self._rear = new_node
    
        self._front = new_node
        self._count += 1 

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _List_Node(deepcopy(value), None)
        
        if self._rear is not None:
            self._rear._next = node
        
        else:
            self._front = node
        
        self._rear = node
        self._count += 1
            
        # your code here
        return

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is 
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if i < 0:
            i = 0
        if i >= self._count:
            i = self._count
    
        if i == 0:
            self.prepend(value)
        elif i == self._count:
            self.append(value)
        else:
            prev = None
            current = self._front
            for _ in range(i):
                prev = current
                current = current._next
            node = _List_Node(deepcopy(value), current)
            if prev:
                prev._next = node
            self._count += 1

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key is not found (int)
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        index = 0
        while current is not None:
            if current._value == key:
                return previous, current, index
            previous = current
            current = current._next
            index += 1
        return None, None, -1

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        previous, current, index = self._linear_search(key)
    
        if current is not None:
            if previous is None:
                # Removing the first node
                self._front = self._front._next
                if self._front is None:
                    self._rear = None  # List becomes empty
            else:
                # Removing a middle or last node
                previous._next = current._next
                if current._next is None:
                    self._rear = previous  # Update rear if last node was removed
    
            self._count -= 1
            return current._value
        else:
            return None
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

        node = self._front
        value = node._value
        self._front = self._front._next
        if self._front is None:
            self._rear = None
        self._count -= 1
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        current = self._front
        previous = None
        while current is not None:
            if current._value == key:
                if previous is None:
                    self._front = current._next
                else:
                    previous._next = current._next
                if current._next is None:
                    self._rear = previous
                self._count -= 1
            else:
                previous = current
        current = current._next

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        _, current, _ = self._linear_search(key)
        if current is not None:
            return deepcopy(current._value)  # Return a copy of the found value
        return None 
    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
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
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        _, _, index = self._linear_search(key)
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
        n = self._count
        return -n <= i < n

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

        if i < 0:
            i += self._count
        current = self._front
        for _ in range(i):
            current = current._next
        return deepcopy(current._value)

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The 
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        if i < 0:
            i += self._count
        current = self._front
        for _ in range(i):
            current = current._next
        current._value = deepcopy(value)

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
    # Return True if current is not None (key was found)
        return current is not None

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        max_value = self._front._value
        current = self._front._next
        while current is not None:
            if current._value > max_value:
                max_value = current._value
            current = current._next
        return max_value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        min_value = self._front._value
        current = self._front._next
        while current is not None:
            if current._value < min_value:
                min_value = current._value
            current = current._next
        return min_value

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        count = 0
        current = self._front
        while current is not None:
            if current._value == key:
                count += 1
            current = current._next
        return count

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: lst.reverse()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        self._rear = self._front
        while current is not None:
            next_node = current._next
            current._next = previous
            previous = current
            current = next

    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (recursive algorithm)
        Use: lst.reverse_r()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        def _reverse_recursive(current, previous=None):
            if not current:
                return previous
            next_node = current._next
            current._next = previous
            return _reverse_recursive(next_node, current)
    
        self._front = _reverse_recursive(self._front)
        if self._front is None:
            self._rear = None
        else:
            self._rear = self._front
            while self._rear._next:
                self._rear = self._rear._next

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        seen = set()
        current = self._front
        previous = None
        while current is not None:
            if current._value in seen:
                # Duplicate found; remove it
                if previous is not None:
                    previous._next = current._next
                if current._next is None:  # current is the last node
                    self._rear = previous
            else:
                # No duplicate; add value to seen set
                seen.add(current._value)
                previous = current
            current = current._next if previous is None else previous._next
        self._count = len(seen)

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

            if args[0] < 0:
                # index is negative
                n = self._count + args[0]
            else:
                n = args[0]
            j = 0

            while j < n:
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
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value

    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next 
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        if pln is None or prn is None or pln._next is None or prn._next is None or pln._next == prn._next:
            return  # Cannot swap if either node is None or if they are the same node
    
    # Nodes to swap
        first = pln._next
        second = prn._next
    
        # Swapping the next links
        first_next = first._next
        second_next = second._next
    
        # Check if consecutive
        if first._next == second:
            first._next = second_next
            second._next = first
            pln._next = second
        elif second._next == first:
            second._next = first_next
            first._next = second
            prn._next = first
        else:
            first._next = second_next
            second._next = first_next
            pln._next = second
            prn._next = first
    
        # Update rear if needed
        if self._rear == first:
            self._rear = second
        elif self._rear == second:
            self._rear = first

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a list (List)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        if self._count != target._count:
            return False  # Lists can't be equal if they have different counts

        current = self._front
        target_current = target._front
    
        while current is not None:
            if current._value != target_current._value:
                return False  # Values at the same position are not equal
            current = current._next
            target_current = target_current._next
    
        return True

    def identical_r(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (recursive version)
        Use: b = lst.identical_r(other)
        -------------------------------------------------------
        Parameters:
            rs - another list (List)
        Returns:
            identical - True if this list contains the same values 
                as other in the same order, otherwise False.
        -------------------------------------------------------
        """
        def _identical_recursive(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is not None and node2 is not None:
                return node1._value == node2._value and _identical_recursive(node1._next, node2._next)
            else:
                return False

        return _identical_recursive(self._front, other._front)

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
        slow = self._front
        fast = self._front
        prev = None
    
        # Using the tortoise and hare algorithm to find the middle of the list
        while fast and fast._next:
            prev = slow
            slow = slow._next
            fast = fast._next._next
    
        # Create two new lists
        target1 = List()
        target2 = List()
    
        # Set the first part
        target1._front = self._front
        target1._rear = prev
        if prev:
            prev._next = None  # Split the list
    
        # Set the second part
        target2._front = slow
        if slow:
            current = slow
            while current._next:
                current = current._next
            target2._rear = current
    
        # Reset the original list
        self._front = None
        self._rear = None
        self._count = 0
    
        # Calculate counts for new lists
        if target1._front:
            current = target1._front
            while current:
                target1._count += 1
                current = current._next
    
        if target2._front:
            current = target2._front
            while current:
                target2._count += 1
                current = current._next
    
        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values 
        alternating into the targets. At finish source self is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        current = self._front
        toggle = True  # Toggle between target1 and target2
    
        while current is not None:
            if toggle:
                target1.append(current._value)
            else:
                target2.append(current._value)
            current = current._next
            toggle = not toggle
    
        # Reset the original list
        self._front = None
        self._rear = None
        self._count = 0
    
        return target1, target2

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements. At finish
        self is empty.
        Order of even and odd is not significant.
        (recursive version)
        Use: even, odd = lst.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even numbered elements of the list (List)
            odd - the odd numbered elements of the list (List)
                The List is empty.
        -------------------------------------------------------
        """
        def _split_recursive(current, toggle=True):
            if current is None:
                return None, None
            even, odd = _split_recursive(current._next, not toggle)
            if toggle:
                return _List_Node(current._value, even), odd
            else:
                return even, _List_Node(current._value, odd)
    
        even_head, odd_head = _split_recursive(self._front)
        even_list = List()
        odd_list = List()
        even_list._front = even_head
        odd_list._front = odd_head
    
        # Reconstruct the count and rear for both lists
        current = even_head
        while current is not None:
            even_list._count += 1
            if current._next is None:
                even_list._rear = current
            current = current._next
    
        current = odd_head
        while current is not None:
            odd_list._count += 1
            if current._next is None:
                odd_list._rear = current
            current = current._next
    
        # Reset the original list
        self._front = None
        self._rear = None
        self._count = 0
    
        return even_list, odd_list

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
            previous - pointer to the node previous to the node containing key (_List_Node)
            current - pointer to the node containing key (_List_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        def _search_recursive(previous, current, index):
            if current is None:
                return (None, None, -1)
            elif current._value == key:
                return (previous, current, index)
            else:
                return _search_recursive(current, current._next, index + 1)

        return _search_recursive(None, self._front, 0)
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
        self._front = None
        self._rear = None
        self._count = 0
        set2 = set([node._value for node in source2])
        current = source1._front
        seen = set()
        while current is not None:
            if current._value in set2 and current._value not in seen:
                self.append(current._value)
                seen.add(current._value)
            current = current._next
    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
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
        def _intersect(node1, values2, seen=set()):
            if node1 is None:
                return None
            if node1._value in values2 and node1._value not in seen:
                seen.add(node1._value)
                return _List_Node(node1._value, _intersect(node1._next, values2, seen))
            else:
                return _intersect(node1._next, values2, seen)
        
        values2 = set([node._value for node in source2])
        self._front = _intersect(source1._front, values2)
        self._rear = None
        self._count = 0
        current = self._front
        while current is not None:
            self._rear = current
            self._count += 1
            current = current._next

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
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0
        seen = set()
        for source in (source1, source2):
            current = source._front
            while current:
                if current._value not in seen:
                    self.append(current._value)
                    seen.add(current._value)
                current = current._next

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        def _union(node, seen):
            if node is None:
                return None
            if node._value not in seen:
                seen.add(node._value)
                return _List_Node(node._value, _union(node._next, seen))
            else:
                return _union(node._next, seen)
        
        seen = set()
        front1 = _union(source1._front, seen)
        front2 = _union(source2._front, seen)
        self._front = front1 if front1 is not None else front2  # Assuming non-empty source1 takes precedence
        self._rear = None
        self._count = 0
        current = self._front
        while current is not None:
            self._rear = current
            self._count += 1
            current = current._next

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (recursive algorithm)
        Use: lst.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        def _clean_recursive(node, seen):
            if node is None:
                return None
            if node._value in seen:
                return _clean_recursive(node._next, seen)
            else:
                seen.add(node._value)
                new_node = _List_Node(node._value, _clean_recursive(node._next, seen))
                return new_node
    
        seen = set()
        self._front = _clean_recursive(self._front, seen)
        # Rebuild rear and count
        self._count = len(seen)
        current = self._front
        prev = None
        while current:
            prev = current
            current = current._next
        self._rear = prev

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
        if not self._front:
            return None, None
        
        slow = self._front
        fast = self._front._next
    
        while fast and fast._next:
            slow = slow._next
            fast = fast._next._next
    
        second_half = slow._next
        slow._next = None
    
        target1 = List()
        target2 = List()
        target1._front = self._front
        target2._front = second_half
    
        # Rebuild counts and rears
        target1._count = target1._rear = target2._count = target2._rear = 0
        current = target1._front
        while current:
            target1._rear = current
            target1._count += 1
            current = current._next
    
        current = target2._front
        while current:
            target2._rear = current
            target2._count += 1
            current = current._next
    
        self._front = self._rear = None
        self._count = 0
    
        return target1, target2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key. At finish, self
        is empty.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        current = self._front
        while current:
            next_node = current._next
            current._next = None
            if current._value <= key:
                target1.append(current._value)
            else:
                target2.append(current._value)
            current = next_node
    
        self._front = self._rear = None
        self._count = 0
    
        return target1, target2

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = lst.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -------------------------------------------------------
        """
        new_list = List()
        current = self._front
        while current:
            new_list.append(current._value)
            current = current._next
        return new_list

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = lst.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -----------------------------------------------------------
        """
        def _copy_recursive(node):
            if not node:
                return None
            return _List_Node(node._value, _copy_recursive(node._next))
        
        new_list = List()
        new_list._front = _copy_recursive(self._front)
        current = new_list._front
        prev = None
        while current:
            prev = current
            current = current._next
        new_list._rear = prev
        new_list._count = self._count
        return new_list

    def _move_front_to_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the front
        of the current List. Private helper method.
        Use: self._move_front_to_front(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        # Detach the front node from the source
        node_to_move = source._front
        source._front = source._front._next
        if source._front is None:
            source._rear = None
        source._count -= 1
        
        # Attach the node to the front of the current list
        node_to_move._next = self._front
        self._front = node_to_move
        if self._rear is None:  # if the list was empty
            self._rear = node_to_move
        self._count += 1

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the rear
        of the current List. Private helper method.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        # Detach the front node from the source
        node_to_move = source._front
        source._front = source._front._next
        if source._front is None:
            source._rear = None
        source._count -= 1
    
        # Attach the node to the rear of the current list
        node_to_move._next = None
        if self._rear is not None:
            self._rear._next = node_to_move
        else:
            self._front = node_to_move
        self._rear = node_to_move
        self._count += 1

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
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        while source1._front or source2._front:
            if source1._front:
                self._move_front_to_rear(source1)
            if source2._front:
                self._move_front_to_rear(source2)

    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        def _combine_recursive(source1, source2):
            if not source1._front and not source2._front:
                return None
            node = None
            if source1._front:
                node = source1._front
                source1._front = source1._front._next
                node._next = _combine_recursive(source2, source1)  # Swap source1 and source2 for alternate adding
            elif source2._front:
                node = source2._front
                source2._front = source2._front._next
                node._next = _combine_recursive(source1, source2)
            return node
    
        self._front = _combine_recursive(source1, source2)
        self._rear = None
        self._count = 0
        current = self._front
        while current:
            self._rear = current
            self._count += 1
            current = current._next
    
        source1._front = source1._rear = source2._front = source2._rear = None
        source1._count = source2._count = 0

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
            
            
    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        (iterative version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (List)
        Returns:
            identical - True if this list contains the same values as
                target in the same order, otherwise False. (bool)
        -------------------------------------------------------
        """
        if self._count != target._count:
            identical = False
        else:
            source_node = self._front
            target_node = target._front

            while source_node is not None and source_node._value == target_node._value:
                source_node = source_node._next
                target_node = target_node._next

            identical = source_node is None
        return identical
    
    
    
    def is_identical_r(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        (recursive version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (List)
        Returns:
            identical - True if this list contains the same values as
                target in the same order, otherwise False. (bool)
        -------------------------------------------------------
        """
        if self._count != target._count:
            return False
        
        else:
            return self._is_identical_r_aux(self._front, target._front)
        
    def _is_identical_r_aux(self, current, target):
        if current is None:
            return True
        else:
            return current._value == target._value and self._is_identical_r_aux(current._next, target._next)


    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        left = True

        while self._front is not None:

            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            left = not left
        return target1, target2


    def split_alt_r(self):
        """
        -------------------------------------------------------
        Recursively splits the source list into two target lists with values
        alternating between the targets. After completion, the source list is empty.
        Order of source values is preserved.
        Use: target1, target2 = source.split_alt_r()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        self._split_alt_r_aux(self._front, target1, target2, True)
        self._front = self._rear = None
        self._count = 0
        return target1, target2

    def _split_alt_r_aux(self, current, target1, target2, to_target1):
        if current is None:
            return
        next_node = current._next
        if to_target1:
            target1.append(current._value)
        else:
            target2.append(current._value)
        self._split_alt_r_aux(next_node, target1, target2, not to_target1)



    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
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
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = source2._linear_search(value)

            if current is not None:
                # Value exists in both source lists.
                _, current, _ = self._linear_search(value)

                if current is None:
                    # Value does not appear in target list.
                    self.append(value)

            source1_node = source1_node._next
        return

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
        self._front = None
        self._rear = None
        self._count = 0

        # Start the recursive intersection process
        self._intersection_recursive(source1._front, source2)

    def _intersection_recursive(self, current1, source2):
        if current1 is None:
            return  # Base case: end of source1

        # Check if the current value in source1 is in source2
        _, found_in_source2, _ = source2._linear_search(current1._value)

        if found_in_source2:
            # Check if it's already in the current list to avoid duplicates
            _, found_in_self, _ = self._linear_search(current1._value)

            if not found_in_self:
                # Append to the current list if not already included
                self.append(current1._value)

        # Recursive call with the next node in source1
        self._intersection_recursive(current1._next, source2)


            
    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
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
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in new list.
                self.append(value)
            source1_node = source1_node._next

        source2_node = source2._front

        while source2_node is not None:
            value = source2_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in current list.
                self.append(value)

            source2_node = source2_node._next
        return

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
        self._front = None
        self._rear = None
        self._count = 0

        # Start the recursive union process
        self._union_recursive(source1._front, source2._front)

    def _union_recursive(self, current1, current2):
        if current1 is not None:
            # Check if the current value in source1 is already in the current list
            _, found_in_self, _ = self._linear_search(current1._value)

            if not found_in_self:
                # Append to the current list if not already included
                self.append(current1._value)

            # Recursive call with the next node in source1
            self._union_recursive(current1._next, current2)

        if current2 is not None:
            # Check if the current value in source2 is already in the current list
            _, found_in_self, _ = self._linear_search(current2._value)

            if not found_in_self:
                # Append to the current list if not already included
                self.append(current2._value)

            # Recursive call with the next node in source2
            self._union_recursive(None, current2._next)
        return
    
    

        
    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        self._rear = self._front
        previous = None
        current = self._front

        while current is not None:
            temp = current._next
            current._next = previous
            previous = current
            current = temp

        self._front = previous
        return
    
    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (recursive algorithm)
        Use: source.reverse_r()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        self._rear = self._front
        self._front = self._reverse_recursive(self._front)
        return
    
    def _reverse_recursive(self, current, previous=None):
        if current is None:
            return previous
        next_node = current._next
        current._next = previous
        return self._reverse_recursive(next_node, current)
    
    
"""
-------------------------------------------------------
Array version of the list ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-07"
-------------------------------------------------------
"""
from copy import deepcopy

class List:
    def __init__(self):
        self._values = []

    def __getitem__(self, i):
        assert self._is_valid_index(i), 'Invalid index value'
        return deepcopy(self._values[i])

    def __len__(self):
        return len(self._values)

    def __setitem__(self, i, value):
        assert self._is_valid_index(i), 'Invalid index value'
        self._values[i] = deepcopy(value)

    def __contains__(self, key):
        return self._linear_search(key) > -1

    def _is_valid_index(self, i):
        return -len(self._values) <= i < len(self._values)

    def _linear_search(self, key):
        i = 0
        while i < len(self._values):
            if self._values[i] == key:
                return i
            i += 1
        return -1

    def _swap(self, i, j):
        assert self._is_valid_index(i), 'Invalid index i'
        assert self._is_valid_index(j), 'Invalid index j'
        self._values[i], self._values[j] = self._values[j], self._values[i]

    def append(self, value):
        self._values.append(deepcopy(value))

    def apply(self, func):
        i = 0
        while i < len(self._values):
            self._values[i] = func(self._values[i])
            i += 1

    def clean(self):
        unique_values = []
        i = 0
        while i < len(self._values):
            if self._values[i] not in unique_values:
                unique_values.append(self._values[i])
            i += 1
        self._values = unique_values

    def combine(self, source1, source2):
        while len(source1) > 0 or len(source2) > 0:
            if len(source1) > 0:
                self.append(source1.pop(0))
            if len(source2) > 0:
                self.append(source2.pop(0))

    def copy(self):
        new_list = List()
        i = 0
        while i < len(self._values):
            new_list.append(self._values[i])
            i += 1
        return new_list

    def count(self, key):
        count = 0
        i = 0
        while i < len(self._values):
            if self._values[i] == key:
                count += 1
            i += 1
        return count

    def find(self, key):
        i = self._linear_search(key)
        if i != -1:
            return deepcopy(self._values[i])
        else:
            return None

    def index(self, key):
        return self._linear_search(key)

    def insert(self, i, value):
        if i < 0:
            i = max(0, len(self._values) + i)
        else:
            i = min(i, len(self._values))
        self._values.insert(i, deepcopy(value))

    def intersection(self, source1, source2):
        self._values = []
        unique_values = set(source1._values).intersection(source2._values)
        for value in unique_values:
            self._values.append(value)

    def is_empty(self):
        return len(self._values) == 0

    def __eq__(self, target):
        if len(self._values) != len(target._values):
            return False
        i = 0
        while i < len(self._values):
            if self._values[i] != target._values[i]:
                return False
            i += 1
        return True

    def max(self):
        assert (len(self._values) > 0), 'Cannot find maximum of an empty list'
        max_value = self._values[0]
        i = 1
        while i < len(self._values):
            if self._values[i] > max_value:
                max_value = self._values[i]
            i += 1
        return deepcopy(max_value)

    def min(self):
        assert (len(self._values) > 0), 'Cannot find minimum of an empty list'
        min_value = self._values[0]
        i = 1
        while i < len(self._values):
            if self._values[i] < min_value:
                min_value = self._values[i]
            i += 1
        return deepcopy(min_value)

    def peek(self):
        assert (len(self._values) > 0), 'Cannot peek at an empty list'
        return deepcopy(self._values[0])

    def pop(self, *args):
        assert len(self._values) > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"
        if len(args) == 1:
            i = args[0]
            value = self._values.pop(i)
        else:
            value = self._values.pop()
        return value

    def prepend(self, value):
        self._values.insert(0, deepcopy(value))

    def remove(self, key):
        i = self._linear_search(key)
        if i != -1:
            return self._values.pop(i)
        else:
            return None

    def remove_front(self):
        assert (len(self._values) > 0), 'Cannot remove from an empty list'
        return self._values.pop(0)

    def remove_many(self, key):
        self._values = [value for value in self._values if value != key]

    def reverse(self):
        self._values.reverse()

    def split(self):
        mid = len(self._values) // 2
        target1 = List()
        target2 = List()
        target1._values = self._values[:mid]
        target2._values = self._values[mid:]
        self._values = []
        return target1, target2

    def split_alt(self):
        target1 = List()
        target2 = List()
        toggle = True
        while len(self._values) > 0:
            if toggle:
                target1.append(self._values.pop(0))
            else:
                target2.append(self._values.pop(0))
            toggle = not toggle
        return target1, target2

    def split_apply(self, func):
        target1 = List()
        target2 = List()
        while len(self._values) > 0:
            value = self._values.pop(0)
            if func(value):
                target1.append(value)
            else:
                target2.append(value)
        return target1, target2

    def split_key(self, key):
        target1 = List()
        target2 = List()
        while len(self._values) > 0:
            value = self._values.pop(0)
            if value < key:
                target1.append(value)
            else:
                target2.append(value)
        return target1, target2

    def union(self, source1, source2):
        self._values = list(set(source1._values).union(set(source2._values)))

    def __iter__(self):
        for value in self._values:
            yield value


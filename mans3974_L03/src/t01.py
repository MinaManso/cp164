# t01.py

from copy import deepcopy

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        assert not self.is_empty(), "Cannot pop from an empty stack"
        return self.items.pop()

    def peek(self):
        assert not self.is_empty(), "Cannot peek at an empty stack"
        return self.items[-1]

    def __iter__(self):
        for item in self.items:
            yield item

class Priority_Queue:
    def __init__(self):
        self._values = []
        self._first = None

    def is_empty(self):
        return len(self._values) == 0

    def __len__(self):
        return len(self._values)

    def insert(self, value):
        self._values.append(deepcopy(value))
        self._set_first()

    def peek(self):
        assert len(self._values) > 0, "Cannot peek at an empty priority queue"
        return deepcopy(self._values[self._first])

    def remove(self):
        assert len(self._values) > 0, "Cannot remove from an empty priority queue"
        value = self._values.pop(self._first)
        self._set_first()
        return value

    def _set_first(self):
        if self.is_empty():
            self._first = None
        else:
            highest_priority_index = 0
            for i in range(1, len(self._values)):
                if self._values[i] < self._values[highest_priority_index]:
                    highest_priority_index = i
            self._first = highest_priority_index

    def __iter__(self):
        for value in self._values:
            yield value

def array_to_stack(stack, source):
    while source:
        stack.push(source.pop())
    return

def stack_to_array(stack, target):
    while not stack.is_empty():
        target.insert(0, stack.pop())
    return

def stack_test(source):
    s = Stack()
    for i in source:
        s.push(i)
    
    print("Stack: ", list(s))


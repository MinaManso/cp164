"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-05-26"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Queue_array import Queue

# Constants

"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-05-26"
-------------------------------------------------------
"""
# Imports

# Constants

def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    
    toggle = True
    
    while not source.is_empty():
        value = source.pop()
        
        
        if toggle:
            target1.push(value)
        else:
            target2.push(value)
        
        toggle = not toggle
    
    return target1, target2


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    temp = Stack()
    
    while not source.is_empty():
        temp.push(source.pop())
        
    while not temp.is_empty():
        source.push(temp.pop())
        
    return


# Constants
OPERATORS = "+-*/"

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    tokens = string.split()

    for token in tokens:
        if token.isdigit():  # Check if the token is a digit
            stack.push(float(token))  # Push the number onto the stack
        else:  # The token is an operator
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
            else:
                raise ValueError(f"Unknown operator: {token}")

    answer = stack.pop()
    return answer
    
    
def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    stack = Stack()
    values_out = []
    values_index = 0

    for op in opstring:
        if op == 'S':
            if values_index < len(values_in):
                stack.push(values_in[values_index])
                values_index += 1
            else:
                return None  # Not enough values to push onto the stack
        elif op == 'X':
            if not stack.is_empty():
                values_out.append(stack.pop())
            else:
                return None  # Nothing to pop from the stack
        else:
            return None  # Invalid operation in opstring

    return values_out

    
    
# Imports
from enum import Enum

# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})

def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"
        
    if m not in string:
        return MIRRORED.NOT_MIRRORED

    parts = string.split(m)

    if len(parts) != 2:
        return MIRRORED.INVALID_CHAR

    left, right = parts
    left_stack = Stack()
    right_stack = Stack()

    for char in left:
        if char not in valid_chars:
            return MIRRORED.INVALID_CHAR
        left_stack.push(char)

    for char in right:
        if char not in valid_chars:
            return MIRRORED.INVALID_CHAR
        right_stack.push(char)

    while not left_stack.is_empty() and not right_stack.is_empty():
        if left_stack.pop() != right_stack.pop():
            return MIRRORED.MISMATCHED

    if not left_stack.is_empty():
        return MIRRORED.TOO_MANY_LEFT
    if not right_stack.is_empty():
        return MIRRORED.TOO_MANY_RIGHT

    return MIRRORED.IS_MIRRORED



def queue_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source queues into the current target queue.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target = queue_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        target - a queue (Queue)
    -------------------------------------------------------
    """
    target = Queue()
    
    while not source1.is_empty() or not source2.is_empty():
        if not source1.is_empty():
            target.insert(source1.remove())
        if not source2.is_empty():
            target.insert(source2.remove())

    return target


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Queue()
    target2 = Queue()

    while not source.is_empty():
        value = source.remove()
        if value > key:
            target1.insert(value)
        else:
            target2.insert(value)

    return target1, target2


def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    def helper(x, y):
        if x == 0:
            return y
        if x > 0:
            return helper(x - 1, y - x) + helper(x - 1, y + x)
        return 0
    
    return helper(x, y)
def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    vowels = 'aeiouAEIOU'
    if s == '':
        return 0
    else:
        return (1 if s[0] in vowels else 0) + vowel_count(s[1:])

    
def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    def helper(base, power):
        if power == 0:
            return 1
        elif power > 0:
            return base * helper(base, power - 1)
        else:
            return 1 / helper(base, -power)
    
    result = helper(base, power)
    return result
    
def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    def clean_string(s):
        return ''.join(c.lower() for c in s if c.isalpha())
    
    def helper(s, start, end):
        if start >= end:
            return True
        if s[start] != s[end]:
            return False
        return helper(s, start + 1, end - 1)
    
    cleaned = clean_string(s)
    return helper(cleaned, 0, len(cleaned) - 1)
    
    
def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    def helper(bag, new_set):
        if not bag:
            return new_set
        if bag[0] not in new_set:
            new_set.append(bag[0])
        return helper(bag[1:], new_set)
    
    result = helper(bag, [])
    return result



def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
 1652346    3 Dark City, 1998
  848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print("{:>8} {:>4} {}".format("Hash", "Slot", "Key"))
    print("-" * 40)
    for value in values:
        hash_value = hash(value)
        slot = hash_value % slots
        print("{:>8} {:>4} {}".format(hash_value, slot, value))
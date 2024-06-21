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
from functions import stack_split_alt


# Constants

source_stack = Stack()

for i in range(10,0, -1):
    source_stack.push(i)
    
t1, t2 = stack_split_alt(source_stack)



print("Target 1 stack:", list(t1))
print("Target 2 stack:", list(t2))
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


# Constants

stack = Stack()

for i in range(10,0, -1):
    stack.push(i)


t1,t2 = stack.split_alt()

print("Target 1 stack:", list(t1))
print("Target 2 stack:", list(t2))
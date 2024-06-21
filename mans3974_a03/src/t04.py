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

from Stack_array import Stack


source_stack = Stack()
for i in range(1, 11):  # Push values 1 to 10 onto the stack
    source_stack.push(i)
    
print("Original stack:", list(source_stack))
    
    # Reverse the stack
source_stack.reverse()
    
print("Reversed stack:", list(source_stack))
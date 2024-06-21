"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-06-01"
-------------------------------------------------------
"""
# Imports
from List_array import List
from utilities import array_to_list
from utilities import list_to_array
# Constants

llist = List()
    
    # Source array
source = [1, 2, 3, 4, 5]
print("Source before array_to_list:", source)
    
    # Convert array to list
array_to_list(llist, source)
print("List after array_to_list:", list(llist))
print("Source after array_to_list:", source)
    
    # Target array
target = []
    
    # Convert list to array
list_to_array(llist, target)
print("Target after list_to_array:", target)
print("List after list_to_array:", list(llist))
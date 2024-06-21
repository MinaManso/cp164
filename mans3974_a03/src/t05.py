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


from functions import postfix

expression = "3 4 + 2 * 7 /"
result = postfix(expression)
print(f"Result of '{expression}' is {result}")
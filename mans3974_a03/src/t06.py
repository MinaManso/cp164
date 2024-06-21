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
from functions import reroute

# Constants
opstring = "SSXSXSX"
values_in = [1, 2, 3, 4]
result = reroute(opstring, values_in)
print(f"Result of reroute with '{opstring}' and {values_in} is {result}")
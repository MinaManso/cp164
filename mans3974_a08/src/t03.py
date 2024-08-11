"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-07-05"
-------------------------------------------------------
"""
# Imports

# Constants

from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, comparison_total, letter_table
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"


bst2 = BST()


Letter(bst2, DATA2)


letter_table(bst2)
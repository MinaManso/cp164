"""
-------------------------------------------------------
t02 file_analysis
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-05-11"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze

# Constants

with open('t02.txt', 'r') as fv:
    upp, low, dig, whi, rem = file_analyze(fv)
    print(f'Uppercase: {upp}')
    print(f'Lowercase: {low}')
    print(f'Digits: {dig}')
    print(f'Whitespace: {whi}')
    print(f'Remaining: {rem}')
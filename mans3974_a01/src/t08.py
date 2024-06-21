"""
-------------------------------------------------------
t08.py
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-05-11"
-------------------------------------------------------
"""
# Imports
from functions import pig_latin
# Constants

test_cases = [
        ("apple", "appleway"),
        ("banana", "ananabay"),
        ("Cherry", "Errychay"),
        ("eat", "eatway"),
        ("smile", "ilesmay")
    ]

for word, expected in test_cases:
    result = pig_latin(word)
    assert result == expected, f"Test failed for word '{word}'. Expected '{expected}', got '{result}'"
    print(f"Test passed for word '{word}'. Pig Latin: '{result}'")



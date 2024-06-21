"""
-------------------------------------------------------
t09.py
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-05-11"
-------------------------------------------------------
"""
# Imports
from functions import substitute

# Constants

test_cases = [
        ("hello world", "ZYXWVUTSRQPONMLKJIHGFEDCBA", "SVOOL DLIOW"),
        ("abcdef", "BCDEFGHIJKLMNOPQRSTUVWXYZA", "BCDEFG"),
        ("123 hello, world!", "BCDEFGHIJKLMNOPQRSTUVWXYZA", "123 IBCDD, VMQKC!"),
        ("HELLO", "QWERTYUIOPASDFGHJKLZXCVBNM", "ITSSG"),
        ("", "QWERTYUIOPASDFGHJKLZXCVBNM", "")
    ]

for string, ciphertext, expected in test_cases:
    result = substitute(string, ciphertext)
    assert result == expected, f"Test failed for string '{string}'. Expected '{expected}', got '{result}'"
    print(f"Test passed for string '{string}'. Enciphered: '{result}'")

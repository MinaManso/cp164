"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mina Mansour
ID:      210139740
Email:   mans3974@mylaurier.ca
__updated__ = "2024-07-03"
-------------------------------------------------------
"""
# Imports

# Constants

# Assuming the BST class and _BST_Node are defined in a file named bst.py

from BST_linked import BST

tree = BST()
tree.insert(5)
tree.insert(6)
tree.insert(3)
tree.insert(1)
tree.insert(4)
tree.insert(8)


'''
print(tree.is_valid())
tree._root._right._value = 4
print(tree.is_valid())
'''
'''
tree2 = BST()
for i in range(1,7):
    tree2.insert(i)
'''
print(tree.levelorder())
tree.remove(3)
print(tree.levelorder())
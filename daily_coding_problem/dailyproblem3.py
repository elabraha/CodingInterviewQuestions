# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

# I needed help wit this oneself.
# Need to work on binary trees and recursion
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_walk(node, str):
    if node:
        str.append(node.val)
        tree_walk(node.left, str)
        tree_walk(node.right, str)
    else:
        str.append("null")

def serialize(node):
    serial_str = []
    tree_walk(node, serial_str)
    serial_str = ', '.join(serial_str)
    return serial_str

def tree_build(serial_list):
    if serial_list[0] == 'null':
        serial_list.pop(0)
        return None;
    root = Node(serial_list.pop(0), tree_build(serial_list), tree_build(serial_list))
    return root


def deserialize(serial_str):
    serial_list = serial_str.split(', ')
    return tree_build(serial_list)

def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    if deserialize(serialize(node)).left.left.val == 'left.left':
        print("Yayy!")

main()

# A unival tree (which stands for "universal value") is a tree where all nodes
# under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
# We will be sending the solution tomorrow, along with tomorrow's question. As
# always, feel free to shoot us an email if there's anything we can help with.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_trees(node, counter=0):
    if node == None:
        return counter
    if (node.left == None and node.right == None):
        counter+=1
    elif (node.left == None and node.right != None:
        if node.right.data == node.data:
            counter+=1
    elif (node.right == None and node.left != None):
        if node.left.data == node.data:
            counter+=1
    left = count_trees(node.left, counter)
    right = count_trees(node.right, counter)

def main():
    root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    print(count_trees(root))

main()

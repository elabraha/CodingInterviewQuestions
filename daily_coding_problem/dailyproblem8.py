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

# I did not do a very good job.
# I really need to get better at recursion and binary trees.

def count_trees(node, c):
    if node is None:
        return True
    left = count_trees(node.left, c)
    right = count_trees(node.right, c)
    if left == False or right == False:
        return False
    if node.left and node.right:
        if node.left.val != node.val:
            return False
    if node.right and node.left:
        if node.right.val != node.val:
            return False
    c[0]+=1
    return True


def main():
    counter = [0]
    root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    count_trees(root, counter)
    print(counter[0])

main()

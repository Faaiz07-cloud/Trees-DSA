# Binary Trees:
# A type of tree in which a node have at-most 2 child nodes.

# Data
nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]

# Values with (-) are null means no child nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

index = 0

def binary_tree():
    global index

    if index >= len(nodes):
        return None

    value = nodes[index]
    index = index + 1

    if value == -1:
        return None

    node = Node(value)
    node.left = binary_tree()
    node.right = binary_tree()

    return node

root = binary_tree()

def print_tree_inorder(node):
    if node is None:
        return
    print_tree_inorder(node.left)
    print(node.data, end=" ")
    print_tree_inorder(node.right)

print_tree_inorder(root)

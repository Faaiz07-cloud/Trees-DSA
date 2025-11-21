"""
This code builds a binary tree from given postorder + inorder lists
and prints its preorder, inorder, and postorder traversals.
"""

Postorder = [1, 4, 7, 6, 3, 13, 14, 10, 8]
Inorder = [1, 3, 4, 6, 7, 8, 10, 13, 14]

post_index = len(Postorder) - 1

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(ino):
    global post_index

    if not ino:
        return None

    value = Postorder[post_index]
    post_index -= 1

    node = Node(value)

    index = ino.index(value)

    node.right = build_tree(ino[index+1:])
    node.left = build_tree(ino[:index])

    return node

root = build_tree(Inorder)

def preorder(node):
    if node is None:
        return
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")

print("Preorder Traversal:")
preorder(root)

print("")
print("")

print("Inorder Traversal:")
inorder(root)

print("")
print("")

print("Postorder Traversal:")
postorder(root)

print("")


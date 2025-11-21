"""
This code builds a binary tree from given preorder + inorder lists
and prints its preorder, inorder, and postorder traversals.
"""

Preorder = [20, 15, 10, 18, 30, 25, 35]
Inorder = [10, 15, 18, 20, 25, 30, 35]

pre_index = 0

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(ino):
     global pre_index

     if not ino:
         return None

     value = Preorder[pre_index]
     pre_index = pre_index + 1

     node = Node(value)

     index = ino.index(value)

     node.left = build_tree(ino[:index])
     node.right = build_tree(ino[index+1:])

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

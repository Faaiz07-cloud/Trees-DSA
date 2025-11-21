"""
This code constructs a binary tree from a list with -1 as null markers
and performs root, preorder, inorder, and postorder traversals.
"""

values = [10, 5, 2, -1, -1, 7, -1, -1, 15, 12, -1, -1, 20, -1, -1]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

index = 0

def build_tree():
     global index

     if index >= len(values):
         return None

     value = values[index]
     index = index + 1

     if value == -1:
         return None

     node = Node(value)

     node.left = build_tree()
     node.right = build_tree()

     return node

root = build_tree()

def root_value(node):
    if node is None:
        return
    print(node.data)

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


print("Root Value:")
root_value(root)

print("")

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


# Binary Search Tree - BST with Pre-order Traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # if tree is empty
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    # if tree has nodes
    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def preorder(self):
        print("Preorder Traversal")
        self._pre_order(self.root)

    def _pre_order(self, node):
        if node:
            print(node.data, end=" ")
            self._pre_order(node.left)
            self._pre_order(node.right)

values = [50, 30, 70, 20, 40, 60, 80]
bst = BST()
for value in values:
    bst.insert(value)

bst.preorder()
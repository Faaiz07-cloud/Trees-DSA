"""
This code implements a Binary Search Tree (BST) with insertion & deletion
and prints its preorder, inorder, and postorder traversals.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # ---------- insert ----------

    # when tree is empty
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    # when tree has some nodes
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
    # ---------- insert ----------

    # ---------- deletion ----------
    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self._delete(node.left, data)

        elif data > node.data:
            node.right = self._delete(node.right, data)

        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: get inorder successor (smallest in right subtree)
            temp = BinarySearchTree._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)

        return node

    @staticmethod
    def _min_value_node(node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    # ---------- deletion ----------

    # ---------- preorder traversal ----------
    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, node):
        if node:
            print(node.data, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)
    # ---------- preorder traversal ----------

    # ---------- inorder traversal ----------
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=" ")
            self._inorder(node.right)
    # ---------- inorder traversal ----------

    # ---------- postorder traversal ----------
    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.data, end=" ")
    # ---------- postorder traversal ----------

values = [25, 15, 50, 10, 22, 35, 70]

bst = BinarySearchTree()
for val in values:
    bst.insert(val)

print("Preorder Traversal:")
bst.preorder()

print("")
print("")

print("Inorder Traversal:")
bst.inorder()

print("")
print("")

print("Postorder Traversal:")
bst.postorder()

print("")
print("")
print("---------------------------------------")
print("")


print("Original BST Inorder Traversal:")
bst.inorder()
print("\n")

# Delete a leaf node
bst.delete(10)
print("After deleting leaf node 10 (Inorder):")
bst.inorder()
print("\n")

# Delete a node with one child
bst.delete(50)
print("After deleting node 50 with one child (Inorder):")
bst.inorder()
print("\n")

# Delete a node with two children
bst.delete(25)
print("After deleting node 25 with two children (Inorder):")
bst.inorder()
print("")






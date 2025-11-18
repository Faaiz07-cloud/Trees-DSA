pre_order = [1, 2, 4, 8, 9, 10, 11,5, 3, 6, 7]
in_order = [8, 4, 10, 9,  11, 2, 5, 1, 6, 3, 7]

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

pre_order_index = 0

def build_tree(ino):
    global pre_order_index

    if not ino:
        return None

    value = pre_order[pre_order_index]
    pre_order_index += 1

    node = Node(value)

    index = ino.index(value)

    node.left = build_tree(ino[:index])
    node.right = build_tree(ino[index+1:])

    return node


root = build_tree(in_order)

def preorder_print(node):
    if not node:
        return
    print(node.value, end=' ')
    preorder_print(node.left)
    preorder_print(node.right)

def inorder_print(node):
    if not node:
        return
    inorder_print(node.left)
    print(node.value, end=' ')
    inorder_print(node.right)


preorder_print(root)
print("")
inorder_print(root)



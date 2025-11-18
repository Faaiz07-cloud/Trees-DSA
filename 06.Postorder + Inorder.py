post_order = [9,1,2,12,7,5,3,11,4,8]
in_order = [9,5,1,7,2,12,8,4,3,11]

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

post_order_index = len(post_order) - 1 # Because root is at last index

def build_tree(ino):
    global post_order_index

    if not ino:
        return None

    value = post_order[post_order_index]
    post_order_index -= 1

    node = Node(value)

    index = ino.index(value)

    node.right = build_tree(ino[index+1:])
    node.left = build_tree(ino[:index])

    return node

root = build_tree(in_order)

def postorder_print(node):
    if not node:
        return
    postorder_print(node.left)
    postorder_print(node.right)
    print(node.value, end=' ')

def inorder_print(node):
    if not node:
        return
    inorder_print(node.left)
    print(node.value, end=' ')
    inorder_print(node.right)


postorder_print(root)
print("")
inorder_print(root)
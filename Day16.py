#BST
class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 15)

inorder(root)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# build the tree
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

# inorder: left -> node -> right
def inorder(node):
    if node is None:
        return
    inorder(node.left)          # go left first
    print(node.val, end=" ")    # then visit the node
    inorder(node.right)         # then go right

inorder(root)   # Output: 1 2 3 4 5 6 7
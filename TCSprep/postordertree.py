class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
root=node(4)
root.left=node(3)
root.right=node(5)
root.left.left=node(1)
root.left.right=node(2)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val,end=" ")
postorder(root)
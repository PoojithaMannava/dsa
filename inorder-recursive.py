class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def prinin(root):
    if root is None:
        return
    prinin(root.left)
    print(root.data,end=" ")
    prinin(root.right)


root = Node(95)
root.left = Node(15)
root.right = Node(220)
root.left.left = Node(10)
root.left.right = Node(30)
prinin(root)
    

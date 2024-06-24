class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printpost(root):
    if root is None:
        return
    printpost(root.left)
    printpost(root.right)
    print(root.data,end=" ")

root = Node(95)
root.left = Node(15)
root.right = Node(220)
root.left.left = Node(10)
root.left.right = Node(30)
root.right.left = Node(160)
root.right.right = Node(285)
printpost(root)


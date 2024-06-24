class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printpre(root):
    
    if root is None:
        return
    print(root.data,end=" ")
    printpre(root.left)
    printpre(root.right)

root = Node(95)
root.left = Node(15)
root.right = Node(220)
root.left.left = Node(10)
root.left.right = Node(30)
root.right.left = Node(160)
root.right.right = Node(285)
printpre(root)

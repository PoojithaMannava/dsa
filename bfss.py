class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def bfs(root):
    if root is None:
        return
    ns=[]
    ns.append(root)
    while len(ns)>0:
        print(ns[0].data)
        n=ns.pop(0)
    if n.left is not None:
        ns.append(n.left)
    if n.right is not None:
        ns.append(n.right)
        
        
        



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
bfs(root)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def display(self,):
        tail=self.head
        while tail:##youube
            print(tail.data,end=" ")
            tail=tail.next
    def rotate(self,k):
        
        if k==0:
            return 
       
        curr=self.head
        c=1
        while c<k and curr is not None:
            curr=curr.next
            c=c+1
        if curr is None:
            return
        kth=curr
        while(curr.next is not None):
            curr=curr.next
        curr.next=self.head
        self.head=kth.next
        kth.next=None

            


l=SLL()
n1=Node(10)
n2=Node(20)
n3=Node(30)
l.head=n1
n1.next=n2
n2.next=n3
l.rotate(2)
l.display()

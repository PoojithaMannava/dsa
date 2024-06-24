class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next

    def delep(self,pos):
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        temp.next=temp.next.next

l=SLL()
n1=Node(10)
n2=Node(20)
n3=Node(30)
l.head=n1
n1.next=n2
n2.next=n3
l.delep(1)
l.display()
        
            

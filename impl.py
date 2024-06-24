class Stack:
    def __init__(self):
        self.top=-1
        self.size=1000
        self.arr=[0]*self.size
    def isfull(self):
        if self.top>=self.size-1:
            return "stack is full"
    def isempty(self):
        if self.top==-1:
            return "full"
    def push(self,x):
        if self.isfull():
            return
        self.top=self.top+1
        self.arr[self.top]=x
      
    def pop(self):
        if self.isempty():
            return
        d=self.arr[self.top]
        self.top=self.top-1
    def _top(self):
        return self.arr[self.top]

s=Stack()
s.push(10)
s.push(20)
s.push(30)
print(s._top())
print(s.pop())
        

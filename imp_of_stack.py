class Stack:
    def __init__(self):
        self.top=-1
        self.size=1000
        self.arr=[0]*self.size
    def push(self,x):
        self.top=self.top+1
        self.arr[self.top]=x
    def pop(self):
        if self.top==-1:
            return "empty"
        else:
            d=self.arr[self.top]
            self.top=self.top-1
            return d
    def top(self):
        return self.arr[self.top]

s=Stack()
s.push(10)
s.push(20)
s.push(20)
d=s.top()
print(d)


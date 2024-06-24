class Queue:
    def __init__(self,c):
        self.front=self.rear=0
        self.c=c
        self.q=[]
    def push(self,x):
        if self.c==self.rear:
            return "queu is full"
        else:
            self.q.append(x)
            self.rear=self.rear+1
    def pop(self):
        if self.front==self.rear:
            return "empty"
        else:
            d=self.q[self.front%self.c]
            self.rear=self.rear-1
          
    
            
            
qi=Queue(4)
qi.push(10)
qi.push(20)
print(qi.pop())
print(qi.pop())

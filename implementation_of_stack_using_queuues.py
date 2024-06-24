from collections import deque

class S:
    def __init__(self):
        self.q=deque()
    def size(self):
        return len(self.q)
    def push(self,x):
        s=self.size()
        self.q.append(x)
        for i in range(s):
            self.q.append(self.q.popleft())
    def pop(self):
        return self.q.popleft()
    def top(self):
        pass
st = S()
st.push(1)
st.push(2)
st.push(3)
print("current size: ", st.size())
print(st.pop())
print(st.pop())


        
        

a=list(map(int,input().split()))
k=int(input())
ms=float('-inf')
cs=0
s=0
for i in range(len(a)):
    cs=cs+a[i]
    if i>=k-1:
        if cs>ms:
            ms=cs
        cs=cs-a[s]
        s=s+1
print(ms)
    

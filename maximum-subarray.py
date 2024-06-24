a=[-2,4,5,-1]
cs=0
ms=-10000
for i in range(len(a)):
    cs=cs+a[i]
    if(cs>ms):
        ms=cs
    if(cs<0):
        cs=0
print(ms)

a=[1,3,4,3]
t=int(input())
d={}
cs=0
s=0
e=-1
for i in range(len(a)):
    cs=cs+a[i]
    if cs-t==0:
        s=0
        e=i
        break
    if cs-t in d:
        s=d[cs-t]+1
        e=i
        break
    d[cs]=i
print(s,e)

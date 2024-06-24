a=[-5,4,6,-3,4,-1]
cs=0
t=int(input())
s=0
e=-1
d={}
ml=0
for i in range(len(a)):
    cs=cs+a[i]
    if cs-t==0:
        s=0
        e=i
        ml=max(ml,s-e+1)
        break
    if cs-t in d:
        s=d[cs-t]+1
        e=i
        ml=max(ml,s-e+1)
        break
    d[cs]=i
print(ml)
    

s=input()
t=input()
d={}
e={}
for i in s:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for i in t:
    if i in e:
        e[i]=e[i]+1
    else:
        e[i]=1
if(d==e):
    print("yes")
else:
    print("no")
        

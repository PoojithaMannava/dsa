a=list(map(int,input().split()))
d={}
for i in range(len(a)):
    if a[i] in d:
        d[a[i]]=d[a[i]]+1
    else:
        d[a[i]]=1
for j in d:
    if d[j]==2:
        print(j)

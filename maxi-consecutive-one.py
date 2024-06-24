a=list(map(int,input().split()))
mc=0
c=0
for i in range(len(a)):
    if(a[i]==1):
        c=c+1
        if c>mc:
            mc=c
    else:
        c=0
print(mc)

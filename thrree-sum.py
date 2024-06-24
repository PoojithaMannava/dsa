a=list(map(int,input().split()))
s=[]
a.sort()
for i in range(len(a)-2):
    l=i+1
    r=len(a)-1
    while l<r:
        su=a[i]+a[l]+a[r]
        if(su==0):
            s.append([a[i],a[r],a[l]])
            l=l+1
            r=r-1
        elif(su<0):
            l=l+1
        elif(su>0):
            r=r-1
print(s)

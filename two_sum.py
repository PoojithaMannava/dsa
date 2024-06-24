a=list(map(int,input().split()))
t=int(input())
a.sort()
l=0
r=len(a)-1
while l<r:
    if(a[l]+a[r]==t):
        print("yes")
        break
    elif(a[l]+a[r]<t):
        l=l+1
    elif(a[l]+a[r]>t):
        r=r-1

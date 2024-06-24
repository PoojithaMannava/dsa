a=list(map(int,input().split()))
a.sort()
ma=0
l=0
r=len(a)-1
while l<r:

    ma=max(ma,(r-l)*min(a[l],a[r]))
    if a[l]<a[r]:
        l=l+1
    else:
        r=r-1
print(ma)

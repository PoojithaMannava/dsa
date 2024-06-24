a=list(map(int,input().split()))
minprice=a[0]

mp=0
for i in range(len(a)):
    if(a[i]<minprice):
        minprice=a[i]
    else:
        cp=a[i]-minprice
        if(cp>mp):
            mp=cp
print(mp)

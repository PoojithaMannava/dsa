a=list(map(int,input().split()))
t=int(input())
s={}
for i in range(len(a)):
    if t-a[i] in s:
        print(s[t-a[i]],i)
        break
    s[a[i]]=i


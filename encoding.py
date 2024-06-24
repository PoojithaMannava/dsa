s=input()
s=s+"#"
res=""
c=1
for i in range(len(s)-1):
    if(s[i]==s[i+1]):
        c=c+1
    else:
        res=res+str(c)+s[i]
        c=1
print(res)

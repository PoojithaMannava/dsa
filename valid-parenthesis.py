s=input()
d={"{":"}",
   "(":")",
   "[":"]"
   }
st=[]
for i in s:
    if i in d:
        if st and st[-1]==d[i]:
            st.pop()
        else:
            print("false")
            break
    else:
        st.append(i)
        
        

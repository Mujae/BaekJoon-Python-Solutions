from collections import deque
s = input()

k=0
st=deque()
for i in range(len(s)):
    if s[i]=="<":
        k=1
        if len(st)>0:
            for j in range(len(st)):
                print(st.pop(), end="")
            
    elif s[i]==">":
        k=0
        st.append(s[i])
        for j in range(len(st)):
            print(st.popleft(),end="")
        continue
    elif k==0 and s[i]==" ":
        for j in range(len(st)):
            print(st.pop(),end="")
        print(" ",end="")
        continue
    st.append(s[i])
l = len(st)
if l>0:
    for _ in range(l):
        print(st.pop(),end="")

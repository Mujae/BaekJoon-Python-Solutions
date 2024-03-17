import sys

input = sys.stdin.readline
s = input().rstrip()
c=0#비교변수
l=len(s)
i=0
while i<l:
    mm=0
    c+=1
    cs=len(str(c))
    m=int(s[i:i+min(cs,l-i)])
        
    if m==0:
        mm=1
    k=c
    while True:
        ks=str(k)
        check=0
        for j in range(len(ks)):
            if ks[j]==s[i]:
                check+=1
        if check>0:
            c=k
            break
        else:
            k+=1
    c=k
    i+=check
print(c)

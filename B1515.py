import sys

input = sys.stdin.readline
s = input().rstrip()
c=0#비교변수
l=len(s)
i=0
while i<l:
    c+=1
    k=c
    while True:
        sk=str(k)
        check=0
        lk=len(sk)
        q=0
        for p in range(lk):
            if i+q<l:
                if s[i+q]==sk[p]:
                    check+=1
                    q+=1
        if q>0:
            break
        k+=1
    c=k
    i+=check
print(c)

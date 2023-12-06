import sys

input = sys.stdin.readline

n = int(input())
li=[]
for i in range(n):
    s = input().rstrip()
    if len(s)>1:
        li.append(int(s[2:]))
        continue
    s = int(s)

    if s==2:
        if len(li)>0:
            print(li.pop())
        else:
            print(-1)
    elif s==3:
        print(len(li))
    elif s==4:
        if len(li)>0:
            print(0)
        else:
            print(1)
    else:
        if len(li)>0:
            print(li[-1])
        else:
            print(-1)
            

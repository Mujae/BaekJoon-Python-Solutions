from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    que = deque()
    c=0
    for i in range(1,4):
        que.append(i)
        while que:
            x = que.popleft()
            if x==n:
                c+=1
            if x<n:
                que.append(x+1)
            if x<n-1:
                que.append(x+2)
            if x<n-2:
                que.append(x+3)
            
    print(c)

from collections import deque

n = int(input())

que = deque()
li2=[n]
que.append((n,0,li2))
v=[0]*(n+1)
while que:
    x, c, l = que.popleft()
    if x==1:
        print(c)
        print(*l)
        break
    if x%3==0 and v[x//3]==0:
        l2=l[:]
        v[x//3]=1
        l2.append(x//3)
        que.append((x//3,c+1,l2))
    if x%2==0 and v[x//2]==0:
        v[x//2]=1
        l2=l[:]
        l2.append(x//2)
        que.append((x//2, c+1,l2))
    if x>1 and v[x-1]==0:
        v[x-1]=1
        l2=l[:]
        l2.append(x-1)
        que.append((x-1,c+1,l2))

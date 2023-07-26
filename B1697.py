from collections import deque
n, m = map(int, input().split())
li=[0]*100001
que = deque()
que.append((n,0))#x, count
while que:
    x, c = que.popleft()
    if x==m:
        print(c)
        break
    if x*2<=100000:
        if li[x*2]==0:
            li[x*2]=1
            que.append((x*2,c+1))
    if x+1<=100000:
        if li[x+1]==0:
            li[x+1]=1
            que.append((x+1,c+1))
    if x>0:
        if li[x-1]==0:
            li[x-1]=1
            que.append((x-1, c+1))

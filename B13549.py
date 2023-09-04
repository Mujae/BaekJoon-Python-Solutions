from collections import deque
n, m = map(int, input().split())
li=[0]*100001
li2=[0]*100001
que = deque()
que.append((n,0))#x, count
t = 100000000
while que:
    x, c = que.popleft()
    if x==m:
        if c<t:
            t=c
        continue
    if x*2<=100000 and x*2 < m*2:
        if li[x*2]==0:
            li[x*2]=1
            que.appendleft((x*2,c))
    if x+1<=100000:
        if li2[x+1]==0:
            li2[x+1]=1
            que.append((x+1,c+1))
    if x>0:
        if li2[x-1]==0:
            li2[x-1]=1
            que.append((x-1, c+1))
print(t)

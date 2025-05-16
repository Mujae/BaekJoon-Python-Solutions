import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
li = []
s=0
count=0

for i in range(N):
    l = list(map(int, input().split()))
    s+=sum(l)
    li.append(l)

n = [1, -1, 0, 0]
m = [0, 0, 1, -1]

while s>0:
    count+=1
    que = deque()
    que.append((0,0))
    li2 = [[0]*M for _ in range(N)]
    while que:
        x, y = que.popleft()
        for i in range(4):
            if 0<=x+n[i]<N and 0<=y+m[i]<M:
                if li[x+n[i]][y+m[i]]==0 and li2[x+n[i]][y+m[i]]==0:
                    li2[x+n[i]][y+m[i]]=1
                    que.append((x+n[i], y+m[i]))

    for i in range(N):
        for j in range(M):
            if li[i][j]==1:
                c=0
                for k in range(4):
                    if 0<=i+n[k]<N and 0<=j+m[k]<M:
                        if li[i+n[k]][j+m[k]]==0 and li2[i+n[k]][j+m[k]]==1:
                            c+=1
                if c>1:
                    s-=1
                    li2[i][j]=-1
    for i in range(N):
        for j in range(M):
            if li[i][j]==1:
                li[i][j]+=li2[i][j]

print(count)          

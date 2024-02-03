import sys
from collections import deque

def bfs(x1, y1):
    global n, m
    if x1+1<n:
        if visited[x1+1][y1]==0:
            visited[x1+1][y1]=1
            que.append((x1+1,y1))
    if x1-1>0:
        if visited[x1-1][y1]==0:
            visited[x1-1][y1]=1
            que.append((x1-1,y1))
    if y1+1<m:
        if visited[x1][y1+1]==0:
            visited[x1][y1+1]=1
            que.append((x1,y1+1))
    if y1-1>0:
        if visited[x1][y1-1]==0:
            visited[x1][y1-1]=1
            que.append((x1,y1-1))
                    

input = sys.stdin.readline

#양양죽겠제~
n, m = map(int, input().split())
visited = [[0]*m for _ in range(n)]
li = []
que=0
wolf=0
sheep=0
for _ in range(n):
    li.append(input().rstrip())
print(li)
for i in range(n):
    for j in range(m):
        if visited[i][j]==0:
            que = deque()
            que.append((i, j))
            visited[i][j]=1
            O=0
            V=0
            while que:
                x, y = que.popleft()
                if li[x][y]=='o':
                    O+=1
                elif li[x][y]=='v':
                    V+=1
                elif li[x][y]=='#':
                    continue
                bfs(x,y)
            if V>=O:
                wolf+=V
            else:
                sheep+=O
print(sheep, wolf)

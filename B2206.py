import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

map1 = []
for i in range(n):
    map1.append([])
    for j in input().rstrip():
        map1[-1].append(int(j))

#0이 이동할 수 있는 곳, 1이 벽일 때 한 개 이하의 벽을 부수고 최단 경로로 이동하는 경우를 구하기
q = deque()
q.append((0,0,1,0))
k=0
while q:
    x, y, c,cw = q.popleft()
    
    if x==n-1 and y==m-1:
        k=c
        print(c)
        break
    
    if x<n-1:
        if map1[x+1][y]==0:
            q.append((x+1,y,c+1,cw))
            map1[x+1][y]==2
        elif map1[x+1][y]==1 and cw==0:
            q.append((x+1,y,c+1,cw+1))
            map1[x+1][y]==2
    if y<m-1:
        if map1[x][y+1]==0:
            map1[x][y+1]==2
            q.append((x,y+1,c+1,cw))
        elif map1[x][y+1]==1 and cw==0:
            q.append((x,y+1,c+1,cw+1))
            map1[x][y+1]==2
    if x>0:
        if map1[x-1][y]==0:
            map1[x-1][y]==2
            q.append((x-1,y,c+1,cw))
        elif map1[x-1][y]==1 and cw==0:
            q.append((x-1,y,c+1,cw+1))
            map1[x-1][y]==2
    if y>0:
        if map1[x][y-1]==0:
            map1[x][y-1]==2
            q.append((x,y-1,c+1,cw))
        elif map1[x][y-1]==1 and cw==0:
            map1[x][y-1]==2
            q.append((x,y-1,c+1,cw+1))

if k==0:
    print(-1)
    

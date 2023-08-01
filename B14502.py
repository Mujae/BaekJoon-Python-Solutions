import sys
input = sys.stdin.readline
from collections import deque

#이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다.
#새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
#0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳, 벽이 없으면 바이러스는 아무곳이나 감

def go(x, y):
    global c, xd, yd, n, m
    if c==3:
        que = deque(li2)
        li4=[wo[:] for wo in li]
        while que:
            x, y = que.popleft()
            if y+1<m:
                if li4[x][y+1]==0:
                    li4[x][y+1]=2
                    que.append((x,y+1))
            if x+1<n:
                if li4[x+1][y]==0:
                    li4[x+1][y]=2
                    que.append((x+1,y))
            if y>0:
                if li4[x][y-1]==0:
                    li4[x][y-1]=2
                    que.append((x,y-1))
            if x>0:
                if li4[x-1][y]==0:
                    li4[x-1][y]=2
                    que.append((x-1,y))
        count=0
        for k in range(n):
            for p in range(m):
                if li4[k][p]==0:
                    count+=1
        li3.append(count)
        return        
    for k in range(n):
        for p in range(m):
            if li[k][p]==0:
                c+=1
                li[k][p]=1
                go(k,p)
                li[k][p]=0
                c-=1


n, m = map(int, input().split())
li =[]#map
li2 =[] #바이러스 위치
for i in range(n):
    li.append(list(map(int, input().split())))
    for j in range(m):
        if li[i][j]==2:
            li2.append((i,j))
li3=[]#생존 너비 저장
c=0
for i in range(n):
    for j in range(m):
        if li[i][j]==0:
            c+=1
            li[i][j]=1
            go(i, j)
            li[i][j]=0
            c-=1
print(max(li3))

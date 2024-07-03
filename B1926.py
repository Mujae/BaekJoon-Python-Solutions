import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

li = []
dx=[1,0,-1,0]
dy=[0,1,0,-1]
for _ in range(n):
    li.append(list(map(int, input().split())))
que=deque()

ma=0
count=0
for k in range(n):
    for j in range(m):
        if li[k][j]==1:
            que.append((k,j))
            li[k][j]=0
            count+=1
            c=0
            while que:
                x, y = que.popleft()
                c+=1
                for i in range(4):
                    if x+dx[i]>-1 and x+dx[i]<n and y+dy[i]>-1 and y+dy[i]<m:
                        if li[x+dx[i]][y+dy[i]]==1:
                            
                            que.append((x+dx[i],y+dy[i]))
                            li[x+dx[i]][y+dy[i]]=0
                            
            ma=max(ma,c)
                
    
print(count)
print(ma)

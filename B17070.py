import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

m = []

for i in range(N):
    m.append(list(map(int, input().split())))

# 대각선으로 가는거 고려
# 전진 무조건 해야하는거 같은데 갈 수 있는 방향이 빈칸이면 가는거임 아니면 저장 안하고 BFS

que = deque()#방향은 오른쪽0, 대각선1, 아래2
que.append((0,1,0))

count = 0
while que:
    x, y, d = que.pop()

    if x+y == (N-1)*2:
        count+=1
        continue
    if d == 0:
        if y+1 < N:
            if m[x][y+1] == 0:
                que.append((x,y+1,0))
        if x+1 < N and y+1 < N:
            if m[x+1][y] + m[x+1][y+1] + m[x][y+1] == 0:
                que.append((x+1,y+1,1))
    elif d == 1:
        if y+1 < N:
            if m[x][y+1] == 0:
                que.append((x,y+1,0))
        if x+1 < N and y+1 < N:
            if m[x+1][y] + m[x+1][y+1] + m[x][y+1] == 0:
                que.append((x+1,y+1,1))
        if x+1<N:
            if m[x+1][y] == 0:
                que.append((x+1,y,2))
    elif d == 2:
        if x+1 < N and y+1 < N:
            if m[x+1][y] + m[x+1][y+1] + m[x][y+1] == 0:
                que.append((x+1,y+1,1))
        if x+1<N:
            if m[x+1][y]==0:
                que.append((x+1,y,2))
print(count)

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append([])
    for j in input().rstrip():
        graph[-1].append(int(j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
k=0

q = deque()
q.append((0, 0, 0))

while q:
    a, b, c = q.popleft()
    if a == n - 1 and b == m - 1:
        k=1
        print(visited[a][b][c])
        break
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 1 and c == 0 :
            visited[nx][ny][1] = visited[a][b][0] + 1
            q.append((nx, ny, 1))
        elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
            visited[nx][ny][c] = visited[a][b][c] + 1
            q.append((nx, ny, c))

if k==0:
    print(-1)
    

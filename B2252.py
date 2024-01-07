from collections import deque
import sys

input = sys.stdin.readline

#백트래킹 방식으로 가보자
def dfs(v):
    visited[v]=1
    for j in li[v]:
        if visited[j]==0:
            dfs(j)
    TS.appendleft(v)
    return

n, m = map(int, input().split())

#4 2 이런식으로 입력되면 4가 2보다 앞에 있으니 4에서 2로 간다고 생각해도 됨
li = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    li[a].append(b)

visited = [0]*(n+1)
TS = deque()

for i in range(1,n+1):
    if visited[i]==0:
        dfs(i)

print(*TS)

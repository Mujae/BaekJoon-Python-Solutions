import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
Inf = int(1e9)
edge = [[Inf]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            edge[i][j]=0

for i in range(k):
    a, b, c = map(int, input().split())
    if edge[a][b]>c:
        edge[a][b]=c

for k in range(1,1+n):
    for i in range(1,1+n):
        for j in range(1,1+n):
            edge[i][j] = min(edge[i][j], edge[i][k] + edge[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if edge[i][j]==Inf:
            print(0, end=" ")
        else:
            print(edge[i][j],end=" ")
    print()

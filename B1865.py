import sys

input = sys.stdin.readline

t = int(input())
INF = int(1e9)
while t>0:
    com="NO"
    t-=1
    n, m, w = map(int, input().split())
    edge = []
    dist=[INF]*n
    for i in range(m + w):
        s, e, we = map(int, input().split())
        if i >= m:
            we = -we
        else:
            edge.append((e, s, we))
        edge.append((s, e, we))
    dist[0]=0
    for _ in range(1,n):
        for s, e, weight in edge:
            if s == INF:
                continue
            dist[e-1] = min(dist[e-1], dist[s-1]+weight)
    for s, e, weight in edge:
        if dist[s-1] != INF and dist[s-1]+weight < dist[e-1]:
            com = "YES"
    print(com)

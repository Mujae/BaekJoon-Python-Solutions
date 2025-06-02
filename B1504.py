import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)
        if dist[node] < cost:
            continue
        for neighbor, weight in graph[node]:
            if dist[neighbor] > cost + weight:
                dist[neighbor] = cost + weight
                heapq.heappush(heap, (dist[neighbor], neighbor))
    return dist

dist1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

path1 = dist1[v1] + dist_v1[v2] + dist_v2[N]
path2 = dist1[v2] + dist_v2[v1] + dist_v1[N]

res = min(path1, path2)
print(res if res < float('inf') else -1)

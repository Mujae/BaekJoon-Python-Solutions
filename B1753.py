import sys
import heapq
#1번부터 차례대로 접근해보면서 갱신
input = sys.stdin.readline
INF = sys.maxsize
v, e = map(int, input().split())
k = int(input())
l = [INF]*(v+1)
l[k]=0
li = [[] for _ in range(v+1)]

for i in range(e):
    a, b, c = map(int, input().split())
    li[a].append((c,b))
que = []
heapq.heappush(que, (0,k))


while que:
    q, x= heapq.heappop(que)
    if l[x] < q:
        continue
    
    for w, next_node in li[x]:
        
        next_wei =w+q

        if next_wei < l[next_node]:
            l[next_node] = next_wei
            heapq.heappush(que,(next_wei,next_node))

for i in range(1,v+1):
    if l[i] != INF:
        print(l[i])
    else:
        print('INF')

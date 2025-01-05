import sys
import heapq

input = sys.stdin.readline
c=0

while True:
    N = int(input())

    if N==0:
        break

    c+=1
    li = []
    li2 = [[1e9]*N for _ in range(N)]
    
    for i in range(N):
        li.append(list(map(int, input().split())))

    heap = []
    heapq.heappush(heap, (li[0][0], 0, 0))

    while heap:
        
        z, x, y = heapq.heappop(heap)
        
        if x<N-1:
            if z+li[x+1][y]<li2[x+1][y]:
                li2[x+1][y]=z+li[x+1][y]
                heapq.heappush(heap, (z+li[x+1][y],x+1,y))
        if y<N-1:
            if z+li[x][y+1]<li2[x][y+1]:
                li2[x][y+1]=z+li[x][y+1]
                heapq.heappush(heap, (z+li[x][y+1],x,y+1))

        if x>0:
            if z+li[x-1][y]<li2[x-1][y]:
                li2[x-1][y]=z+li[x-1][y]
                heapq.heappush(heap, (z+li[x-1][y],x-1,y))

        if y>0:
            if z+li[x][y-1]<li2[x][y-1]:
                li2[x][y-1]=z+li[x][y-1]
                heapq.heappush(heap, (z+li[x][y-1],x,y-1))
    
    print(f'Problem {c}:', li2[-1][-1])

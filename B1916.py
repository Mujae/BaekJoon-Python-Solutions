import sys
from collections import deque
import math

input = sys.stdin.readline

N = int(input())
M = int(input())

table = [[100001]*N for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    table[a-1][b-1]=min(table[a-1][b-1], c)

start, end = map(int, input().split())
start-=1
end-=1

que = deque()
que.append((start,0))
li = [math.inf]*N

while que:
    x, accumulated_cost = que.popleft()
    
    for i in range(N):
        if table[x][i]<100001:
            accumulated_cost2 = accumulated_cost+table[x][i]
            if accumulated_cost2<li[i]:
                li[i] = accumulated_cost2
                if i==end:
                    break
                que.append((i, accumulated_cost2))

print(li[end])

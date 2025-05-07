import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())#n은 노드 개수, m은 수색범위, r은 간선 개수
num_li = list(map(int, input().split()))
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(r):
    a, b, c = map(int, input().split())
    graph[a][b]=c
    graph[b][a]=c

def BFS(num):
    global n
    global m
    maximum_items_count=0
    que = deque()
    que.append((num, 0))
    s=set()
    s.add(num)
    
    while que:
        number, count = que.pop()
        for i in range(1, n+1):
            if graph[number][i]>0:
                if count+graph[number][i]<=m:
                    que.append((i, count+graph[number][i]))
                    s.add(i)

    s=list(s)
    for i in range(len(s)):
        maximum_items_count+=num_li[s[i]-1]

    return maximum_items_count

maximum_num = 0
for i in range(1, n+1):
    maximum_num = max(maximum_num, BFS(i))

print(maximum_num)


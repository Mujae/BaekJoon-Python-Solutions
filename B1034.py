import sys

input = sys.stdin.readline

n, m = map(int, input().split())

li=[[] for _ in range(n)]

for i in range(n):
    a = int(input())
    for j in range(m):
        li[i].append(a[j])

k = int(input())


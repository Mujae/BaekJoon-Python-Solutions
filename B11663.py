import sys

input = sys.stdin.readline

N, M = map(int, input().split())

li = list(map(int, input().split()))

li2=[]

for _ in range(M):
    li2.append(list(map(int, input().split())))

li2 = sorted(li2)

print(li2)

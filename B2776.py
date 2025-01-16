import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    s = set(list(map(int, input().split())))

    M = int(input())
    li = list(map(int, input().split()))

    for i in range(M):
        if li[i] in s:
            print(1)
        else:
            print(0)

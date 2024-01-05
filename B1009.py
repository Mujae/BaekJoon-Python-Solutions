import sys
input = sys.stdin.readline
li = [[10], [1], [6,2,4,8], [1,3,9,7], [6,4], [5], [6], [1,7,9,3], [6,8,4,2], [1,9]]
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(li[a%10][b%len(li[a%10])])

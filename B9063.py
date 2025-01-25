import sys
input = sys.stdin.readline
N = int(input())

a,b,c,d=10001,10001,-10001,-10001

if N==1:
    print(0)
else:
    for i in range(N):
        x, y = map(int, input().split())
        a = min(a, x)
        b = min(b, y)
        c = max(c, x)
        d = max(d, y)
    print((c-a)*(d-b))
    

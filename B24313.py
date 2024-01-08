a, b = map(int, input().split())

c = int(input())
d = int(input())

if a*d+b <= d*c and a<=c:
    print(1)
else:
    print(0)

import sys

input = sys.stdin.readline

N, L = map(int, input().split())

li = []
c=0
m=0

for i in range(N):
    li.append(tuple(map(int, input().split())))

li = sorted(li)

for i in range(N):
    l = li[i][1] - li[i][0]
    if m>0:
        l-=m
    if l%L==0:
        c+=l//L
        m=0
    else:
        c+=l//L+1
        if i != N-1:
            m = L*(l//L+1) - l - li[i+1][0]+li[i][1]
print(c)


import sys
input=sys.stdin.readline
n = int(input())
li=list(map(int, input().split()))
dp=[0]*(n+1)
m=0
for i in range(n):
    a=li[i]
    b=li[i]
    for j in range(i+1,n):
        if li[j]>b:
            a+=li[j]
            b=li[j]
    m = max(m,a)
print(m)

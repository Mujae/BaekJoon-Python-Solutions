import sys

input = sys.stdin.readline

N, S = map(int, input().split())
li = list(map(int, input().split()))

i, j = 0, 0 #포인터
s, l = 0, N+1 #합, 최소 길

while j<N:
    s+=li[j]
    if s>=S:
        l = min(l, j-i+1)
        while i<j:
            s-=li[i]
            i+=1
            if s>=S:
                l = min(l, j-i+1)
            else:
                break
    j+=1

if l != N+1:
    print(l)
else:
    print(0)

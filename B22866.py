import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

li = list(map(int, input().split()))

m=li[0]
li2 = [0]*N

for i in range(1, N):
    if li[i]>m:
        li2[i]+=1
        m=li[i]

l = sum(li2)

sta = deque([li[0]])

for i in range(1, N):
    if sta[-1]>li[i]:
        sta.append(li[i])
    elif sta[-1]<li[i]:
        while sta:
            if sta[-1]>li[i]:
                break
            sta.pop()
        sta.append(li[i])
    l2 = len(sta)
    if l2 + l -1== 0:
        print(0)
    else:
        print(li[i], len(sta)+l-1)

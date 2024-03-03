import sys
from collections import deque


input = sys.stdin.readline

n = int(input())

for i in range(n):
    li = list(map(int, input().split()))
    a = li[0]
    c=0
    que = deque()   
    for j in li[1:]:
        l=0
        go = len(que)
        for k in range(go):
            if que[k]>j:
                
                c+=go-k
                que.insert(k,j)
                l=1
                break
        if l==0:
            que.append(j)
    print(a, c)
    

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())#사람의 수, 파티의 수
li = list(map(int, input().split()))

if li[0]==0:
    print(M)
else:
    s=set(li[1:])
    que = deque(s)
    count=0
    li2=[]
    li3=[[0]*N for _ in range(N)]
    for i in range(M):
        li2.append(list(map(int, input().split())))
        for j in range(1,li2[-1][0]+1):
            for k in range(1,li2[-1][0]+1):
                 li3[li2[-1][j]-1][li2[-1][k]-1]=1
    
    while que:
        x = que.popleft()

        for i in range(N):
            if li3[x-1][i]==1 and i+1 not in s:
                s.add(i+1)
                que.append(i+1)
    

    for i in range(M):
        c=0
        for j in range(1,li2[i][0]+1):
            if li2[i][j] in s:
                c=1
                break

        if c==0:
            count+=1
    print(count)


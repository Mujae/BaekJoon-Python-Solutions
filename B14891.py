from collections import deque
import sys

input = sys.stdin.readline

li=deque()#0, 2, 5ㄱㅏ 중요

for _ in range(4):
    b=input().rstrip()
    deq=deque()
    for i in range(8):
        deq.append(int(b[i]))
    li.append(deq)
k = int(input())
for _ in range(k):
    n, d = map(int, input().split())
    n-=1
    l=[li[0][6],li[1][6],li[2][6],li[3][6]]
    r=[li[0][2], li[1][2], li[2][2],li[3][2]]
    if d==1:#시계방향 오른쪽은 인덱스3 체크, 왼쪽은 7
        li[n].appendleft(li[n].pop())
        d2=d
        for i in range(n+1,4):
            if l[i]!=r[i-1]:
                d2*=-1
                if d2==1:
                    li[i].appendleft(li[i].pop())
                else:
                    li[i].append(li[i].popleft())
                
            else:
                break
        d2=d
        for i in range(n-1,-1,-1):
            if r[i]!=l[i+1]:
                d2*=-1
                if d2==1:
                    li[i].appendleft(li[i].pop())
                else:
                    li[i].append(li[i].popleft())
                
            else:
                break
    else:
        li[n].append(li[n].popleft())
        d2=d
        for i in range(n+1,4):
            if l[i]!=r[i-1]:
                d2*=-1
                if d2==1:
                    li[i].appendleft(li[i].pop())
                else:
                    li[i].append(li[i].popleft())
                
            else:
                break
        d2=d
        for i in range(n-1,-1,-1):
            if r[i]!=l[i+1]:
                d2*=-1
                if d2==1:
                    li[i].appendleft(li[i].pop())
                else:
                    li[i].append(li[i].popleft())
                
            else:
                break
s=0
if li[0][0]==1:
    s+=1
if li[1][0]==1:
    s+=2
if li[2][0]==1:
    s+=4
if li[3][0]==1:
    s+=8
print(s)

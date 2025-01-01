import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

right_que = deque(map(int, input().split()))
left_que = deque()

for i in range(N):
    c=0
    mr=0
    while left_que:
        if right_que[0]>=left_que[-1][0]:
            left_que.pop()
        else:
            break
        
    left_que.append((right_que.popleft(),i))
    l=left_que[-1][0]
    
    for j in range(len(right_que)):
        if right_que[j]>l:
            l=right_que[j]
            c+=1
            if mr==0:
                mr=i+j+1
                
    if len(left_que) - 1 + c == 0:
        print(0)
    else:
        if len(left_que)==1:#첫번째 or 뒤에 같은 것만 많을 때)
            print(c, mr+1)
        elif i==N-1:
            print(len(left_que)-1,left_que[-1][1]+1)
        else:
            print(len(left_que)-1+c, end = " ")
            if i-left_que[-2][1]<=mr-i:
                print(left_que[-2][1]+1)
            else:
                print(mr+1)
                

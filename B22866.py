import sys
from collections import deque


#왼쪽은 stack, 오른쪽은 매번 탐색하는 코드가 더 깔끔해보였는데 시간초과.
#아래처럼 메모리는 많이 잡아먹어도 그냥 두 번 돌리니깐 통과. 그냥 구현문제 아닌가?

input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
right_que = deque()
left_que = deque()
save_li = [[] for _ in range(N)]

#원래라면 함수 만들어서 이쁘게 관리할텐데.. 다음기회에
#left
for i in range(N):
    while left_que:
        if li[i]>=left_que[-1][0]:
            left_que.pop()
        else:
            break
    left_que.append((li[i],i))
    if len(left_que) > 1:
        save_li[i].append(len(left_que)-1)
        save_li[i].append(left_que[-2][1])
    else:
        save_li[i].append(0)
        save_li[i].append(-1)

#right
for i in range(N-1,-1,-1):
    while right_que:
        if li[i]>=right_que[-1][0]:
            right_que.pop()
        else:
            break
    right_que.append((li[i],i))

    if len(right_que) > 1:
        save_li[i].append(len(right_que)-1)
        save_li[i].append(right_que[-2][1])
    else:
        save_li[i].append(0)
        save_li[i].append(-1)
        
for i in range(N):
    if save_li[i][0]+save_li[i][2]==0:
        print(0)
    else:
        if save_li[i][1]==-1:
            print(save_li[i][2], save_li[i][3]+1)
        elif save_li[i][3]==-1:
            print(save_li[i][0], save_li[i][1]+1)
        elif i-save_li[i][1] <= save_li[i][3]-i:
            print(save_li[i][0]+save_li[i][2], save_li[i][1]+1)
        else:
            print(save_li[i][0]+save_li[i][2], save_li[i][3]+1)
            

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())#ㅂㅗ드의 크기
m = [[0]*n for _ in range(n)]
k = int(input())#사과 개수
xd = [0,1,0,-1]
yd = [1,0,-1,0]
#먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
#만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
#만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다. 자기 몸은 2로 하자 사과는 1
#만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다

for _ in range(k):
    a, b= map(int, input().split())
    m[a-1][b-1]=1
    
li2=deque()#방향
d = int(input())
for _ in range(d):
    q, w=input().rstrip().split()
    li2.append((int(q),w))
que=deque()#몸 관리 해

def go():#p가 현재 사방위 중 어디를 보는지
    global k, ch, que, a, b, p
    a+=xd[p]
    b+=yd[p]
    if a<0 or b>n-1 or b<0 or a>n-1:
        return False
    l2 = len(que)
    for kkk in que:
        if a==kkk[0] and b==kkk[1]:
            return False
    if m[a][b]==1:
        que.append((a,b))
        m[a][b]=0
    else:
        l1=len(que)
        que.append((a,b))
        que.popleft()
    return True

#k가 0이 되면 끝
ch=0
p=0#방향
o=li2[0][0]#첫전진
a=0
b=0
que.append((a,b))
op=0
while o>0:
    o-=1
    ch+=1
    if not go():
        op=1
        break
    
if op==0:
    for i in range(d):
        dl= li2[i][1]
        if dl=='D':
            p+=1
            if p==4:
                p=0
        else:
            p-=1
            if p==-1:
                p=3
        if i!=d-1:
            c = li2[i+1][0]-li2[i][0]
            while c>0:
                ch+=1
                c-=1
                if not go():
                    op=1
                    break
        else:
            while True:
                ch+=1
                if not go():
                    op=1
                    break
        if op==1:
            break
print(ch)


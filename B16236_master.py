#물고기 잡아먹으러 다닐건데 자기보다 작은 물고기만 먹을 수 있고 같은 크기까지는 지나갈 수 있음
#이런 상황에서 최대한의 물고기를 먹을건데 먹을 수 있는 물고기가 여러마리면 거리가 가장 가까운걸 먹어야
#이때 가까운 물고기가 많다면, 가장 위에 있는 물고기 -> 왼쪽에 있는 물고기로 먹어야함
#이동하는데는 1초가 소요되나 먹는데는 시간 소요가 없으니 이동시간만 따지면 됨 -> 먹으면 빈칸으로
#아기 상어는 자신의 크기와 같은 물고기를 먹을 때 마다 크기가 1증가 처음엔 2마리, 나중에 3마리 무야함
#가보자잇
import sys
from collections import deque
mx= 0
my = 0
mt =0
def explore2(a, b, tt):
    global mx, my, mt, l
    if m[a][b]>0 and m[a][b]<l:
        if tt<=mt:
            if a<mx or (a==mx and b<my):
                mx=a
                my=b
                mt=tt
def explore(x1, y1, t):
    global l, count, tm, visited, que, m, mx, my, mt
    
    if m[x1][y1]>0 and m[x1][y1]<l:
        mx = x1
        my = y1
        mt = t
        #현재 들어있는 것들까지는 탐험해봐야함
        while que:
            x2, y2, tix = que.popleft()
            if x2>0:
                explore2(x2-1,y2,tix)
            if y2>0:
                explore2(x2,y2-1,tix)
            if y2<N-1:
                explore2(x2,y2+1,tix)
            if x2<N-1:
                explore2(x2+1,y2,tix)
        count+=1
        tm+=mt+1
        m[mx][my]=0
        if count==l:
            l+=1
            count=0
        #visited 초기화 및 deque 초기화 + 현재 위치 넣기
        que = deque()
        que.append((mx,my,0))
        visited = [[0]*N for _ in range(N)]
        visited[mx][my]=1
        return False
    elif visited[x1][y1]==0 and m[x1][y1]<=l:
        visited[x1][y1]=1
        que.append((x1,y1,t+1))
    return True
input = sys.stdin.readline
N = int(input())
m = []#map
location = (N+1,N+1)
for i in range(N):
    m.append(list(map(int,input().split())))
    #첫 출발 찾을 때까지만 돌리도록
    if location[0]==N+1:
        for j in range(N):
            if m[i][j]==9:
                location = (i, j)
                m[i][j]=0
que = deque()
que.append((location[0],location[1],0))
l=2 #fish-length
count = 0 #feed count
tm = 0 #time
visited = [[0]*N for _ in range(N)]
visited[location[0]][location[1]]=1
#(N-1)+(N-2)까지만 탐색 시키기 vs visited 리스트 계속 update -> 후자가 나은듯
while que:
    x, y, tic = que.popleft()
    if x>0:
        if explore(x-1,y,tic)!=True:
            continue
    if y>0:
        if explore(x,y-1,tic) != True:
            continue
    if y<N-1:
        if explore(x,y+1,tic)!=True:
            continue
    if x<N-1:
        if explore(x+1,y,tic) != True:
            continue

print(tm)




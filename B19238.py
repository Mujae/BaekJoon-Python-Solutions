#행번호 우선 열번호 우선
#승객을 태워 이동한 거리의 두 배만큼 연료 획득
#이동중 연료바닥은 실패 but 목적지로 이동시킨 동시에 바닥은 ㄱㅊ -> 충전된단말이고 중간이면 -1 출
import sys
import heapq
import copy

N, M, O = map(int, input().split())

li = [] #map

for _ in range(N):
    li.append(list(map(int, input().split())))

x, y = map(int, input().split())#start place

for i in range(M):
    a, b, c, d = map(int, input().split())
    li[a-1][b-1]=i+2
    li[c-1][d-1]=i+2+400
    
q = []
heapq.heappush(q,(x-1,y-1,0,O))

w = 0 #0이면 승객 찾는중 1이면 목적지
number = 0 #현재 승객 num

def find_passenger(x,y):
    global N

    if (x>=0 and y>=0) and (x<N and y<N):
        if li[x][y]>1 and li[x][y]<402:
            return 2
        elif li[x][y]!=1:
            return 1
    return 0
        
    
def find_destination(x,y,n):
    global N
    
    if (x>=0 and y>=0) and (x<N and y<N):
        if li[x][y]==400+n:
            return 2
        elif li[x][y]!=1:
            return 1
    return 0
    

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
li2 = copy.deepcopy(li)

while q:
    x, y, m1, m2 = heapq.heappop(q)#m1이 오일 잔여량 m2가 이동하는데 쓴만
    li[x][y]=1
    print(x,y,m1,m2)
    if w == 0:
        for i in range(4):
            if m2>0:
                K = find_passenger(x+dx[i], y+dy[i])
                if  K == 2:
                    q=[]
                    q.append((x+dx[i],y+dy[i], 0, m2-1))
                    w=1
                    number = li[x+dx[i]][y+dy[i]]
                    li2[x+dx[i]][y+dy[i]]=0
                    li = copy.deepcopy(li2)
                    break
                elif K == 1:
                    heapq.heappush(q, (x+dx[i], y+dy[i], 0, m2-1))   
            
    elif w == 1:
        for i in range(4):
            if find_destination(x+dx[i], y+dy[i], number) == 2:
                M-=1
                m2-=1
                if m2==-1:
                    q=False
                    break
                m1+=1
                m2+=m1*2
                if M==0:
                    q=False
                    break
                q=[]
                q.append((x+dx[i], y+dy[i], 0, m2))
                w=0
                li2[x+dx[i]][y+dy[i]]=0
                li = copy.deepcopy(li2)
                break
            elif find_destination(x+dx[i], y+dy[i], number) == 1:
                if m1>0:
                    heapq.heappush(q,(x+dx[i], y+dy[i], m1+1, m2-1))
            
if m1==0 or M>0:
    print(-1)
else:
    print(m1)

    



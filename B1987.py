import sys

input = sys.stdin.readline

li = [0]*26#알파뱃 관리 
m = []#맵 
R, C = map(int, input().split())

for i in range(R):
    m.append(input().rstrip())
    for j in range(C):
        li[ord(m[i][j])-65]=1
        
s = sum(li)#조기종료를 위한 
li=[0]*26

li[ord(m[0][0]) - 65] += 1
i, j = 0, 0

mc = 1

def dfs(x, y, c):
    global R
    global C
    global mc
    if mc==s:
        print(s)
        exit()
    if x+1<R:
        if li[ord(m[x+1][y])-65]==0:
            li[ord(m[x+1][y])-65]=1
            mc= max(c+1, mc)
            dfs(x+1,y,c+1)
            li[ord(m[x+1][y])-65]=0
    if x>0:
        if li[ord(m[x-1][y])-65]==0:
            li[ord(m[x-1][y])-65]=1
            mc = max(c+1, mc)
            dfs(x-1, y, c+1)
            li[ord(m[x-1][y])-65]=0
    if y+1<C:
        if li[ord(m[x][y+1])-65]==0:
            li[ord(m[x][y+1])-65]=1
            mc = max(c+1, mc)
            dfs(x,y+1,c+1)
            li[ord(m[x][y+1])-65]=0
    if y>0:
        if li[ord(m[x][y-1])-65]==0:
            li[ord(m[x][y-1])-65]=1
            mc = max(c+1, mc)
            dfs(x,y-1,c+1)
            li[ord(m[x][y-1])-65]=0
            
    
dfs(i, j, 1)

print(mc)

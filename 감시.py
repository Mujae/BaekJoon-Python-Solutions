import sys

input = sys.stdin.readline

n, m = map(int, input().split())

li = []
li2=[]#위
for i in range(n):
    li.append(list(map(int, input().split())))
    for j in range(m):
        if li[i][j]>0 and li[i][j]<6:
            li2.append((i,j,li[i][j]))
mini = 64
def go (k):
    global n, m, mini
    if k==n:
        for p in range(n):
            for q in range(m):
                if li[p][q]==0:
                    answer+=1
        return min(mini, answer)
    '''
    if li2[k][2]==1:
        for i in range(
    elif li2[k][2]==2:

    elif li2[k][2]==3:

    elif li2[k][2]==4:

    else:
    백트래킹(dfs)로 바꿀 예정'''        

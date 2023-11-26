import sys

def gogo(s1,x,y):
    global li
    
    if s1==405:
        for w in range(9):
            for m in range(9):
                print(li[w][m], end="")
            print()
        exit()
    c=0
    for i in range(x,9):
        for j in range(9):
            if li[i][j]==0:
                x=i
                y=j
                c+=1
                break
        if c==1:
            break
    li2=[1,0,0,0,0,0,0,0,0,0]
    for k in range(9):
        li2[li[x][k]]=1

    for k in range(9):
        li2[li[k][y]]=1
    x1=(x//3)*3
    y1=(y//3)*3
    for k in range(x1,x1+3):
        for t in range(y1,y1+3):
            li2[li[k][t]]=1

    for k in range(1,10):
        if li2[k]==0:
            li[x][y]=k
            gogo(s1+k,x,y)
            li[x][y]=0
            
input = sys.stdin.readline

li=[]
s=0
for _ in range(9):
    o = input().rstrip()
    li2=[]
    for i in range(9):
        s+=int(o[i])
        li2.append(int(o[i]))
    li.append(li2)
    
gogo(s,0,0)

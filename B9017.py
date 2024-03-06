import sys

input = sys.stdin.readline

T = int(input())

while T>0:
    T-=1
    n = int(input())
    li = list(map(int, input().split()))
    m=max(li)
    li0=[]
    for i in range(1,m+1):
        c=0
        for j in range(n):
            if li[j]==i:
                c+=1
            if c==6:
                li0.append(i)
                break
    c=0
    cor = [i+1 for i in range(n)]
    for i in range(n):
        if li[i] not in li0:
            c+=1
        cor[i]-=c
    li2 = [[] for _ in range(m+1)]
    for i in range(n):
        li2[li[i]].append(cor[i])
    
    li3=[]
    for i in range(m+1):
        if len(li2[i])==6:
            li3.append([sum(li2[i][:4]),li2[i][4], i])
    li3 = sorted(li3, key= lambda x: (x[0], x[1]))
    print(li3[0][2])

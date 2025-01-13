import sys

input = sys.stdin.readline

n, k = map(int, input().split())

li = set()

for i in range(n):
    li.add(int(input()))

li = sorted(list(li))

li2 = [[0]*n for _ in range(k+1)]
for i in range(1,k+1):
    if li2[i-1][0]+li[i]:
        li2[i][0]=li2[i-1][0]+li[i]
        
l = len(li)
for i in range(1, l):
    for j in range(1,k+1):
        if li2[j][i-1]+li[i]<=j:
            li2[j][i]=li2[j-1][i]+li[i]
        else:
            m=0
            if k-li2[j-1][i]>0:
                li2[j][i] = (li2[j-1][i]+li2[k-li2[j-1][i]][i-1],li2[j-1][i][1]+1)
            
        
c=0
for i in range(l):
    if li2[-1][i]==k:
        c

import sys

input = sys.stdin.readline

n, m = map(int,input().split())

li=[]

for _ in range(n):
    li.append(list(map(int,input().split())))

def mul(x,y):
    global n
    li2=[]
    for k in range(n):
        a=[]
        for i in range(n):
            b=0
            for j in range(n):
                b+=(x[k][j]*y[j][i])
            a.append(b%1000)
        li2.append(a)
    return li2

def square(s, B):
    if B==1:
        for i in range(n):
            for j in range(n):
                s[i][j] %= 1000
        return s
    new = square(s,B//2)
    if B%2==0:
        return mul(new, new)
    else:
       
        return mul(mul(new,new),s)

answer = square(li,m)
for i in answer:
    print(*i)

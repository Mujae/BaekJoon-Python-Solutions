import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    li = list(map(int, input().split()))
    k=0
    s=li[0]
    for j in range(1,3):
       if li[j]>s:
           k=j
           s=li[j]
    print(f'Scenario #{i+1}:')
    m=0
    if k==0:
        if pow(s,2)==pow(li[1],2)+pow(li[2],2):
            m=1
    elif k==1:
        if pow(s,2)==pow(li[0],2)+pow(li[2],2):
            m=1
    else:
        if pow(s,2) == pow(li[0],2) + pow(li[1],2):
            m=1
    if m==1:
        print('yes')
    else:
        print('no')
    if i-1!=n:
        print(' ')
    

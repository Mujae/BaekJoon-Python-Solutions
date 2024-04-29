import sys

input = sys.stdin.readline

li=[0,0,0]#l k p

for _ in range(3):
    s=input()
    if s[0] =='l':
        li[0]=1
    elif s[0]=='k':
        li[1]=1
    elif s[0]=='p':
        li[2]=1

if sum(li)==3:
    print('GLOBAL')
else:
    print('PONIX')
    

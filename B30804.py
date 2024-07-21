import sys

input = sys.stdin.readline
N = int(input())
li = list(map(int,input().split()))
#왼부터 l이 2인 선에서 모양 늘려가면서
mc=0
if N==1:
    print(1)
    exit()
s={li[0]}
l=1
c=1
c1=1
mc=0
b=1
while b<N:
    print(b,c)
    print(s)
    if li[b] not in s:
        l+=1
        if l==2:
            s.add(li[b])
            c+=1
        elif l==3:
            s=set((li[b-1],li[b]))
            l=2
            c1=c-c1+1
            mc=max(mc,c)
            c=c1
    else:
        if l==1:
            c1+=1
            c+=1
        else:
            c+=1
    mc=max(mc,c)
    b+=1
    
    
print(mc)
    
    #처음 안맞은 곳에 a가 가고 b는 바뀐데부터 시작하면 

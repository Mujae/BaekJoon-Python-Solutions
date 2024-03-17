import sys
input = sys.stdin.readline

N,M = map(int, input().split())

li = list(map(int, input().split()))
su=sum(li[:M])
s=su
c=1
for i in range(1,N-M+1):
    su = su-li[i-1]+li[i+M-1]
    if s<su:
        c=1
        s=su
    elif s==su:
        c+=1


if s==0:
    print('SAD')
else:
    print(s)
    print(c)

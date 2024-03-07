import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
placement=list(map(int,input().split()))

ma=0
if m ==1:
    print(max(placement[0],n-placement[0]))
else:
    for i in range(m):
        if i==0:
            ma=max(placement[i],ma)
            ma=max((1+placement[i+1]-placement[i])//2,ma)
        elif i==m-1:
            ma=max(n-placement[i],ma)
        else:
            ma=max((1+placement[i+1]-placement[i])//2,ma)
    print(ma)
            

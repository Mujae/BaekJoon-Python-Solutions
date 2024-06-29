import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

def div(n):
    if n<=2:
        return dic[n]
    elif dic[n]>0:
        return dic[n]
    else:
        h=n//2
        if n%2==0:
            dic[n]=(2*div(h-1)*div(h) + div(h)**2)%1000000007
            return dic[n]
        else:
            dic[n]=(div(h+1)**2 + div(h)**2)%1000000007
            return dic[n]
    
dic = defaultdict(int)
dic[0]=0
dic[1]=1
dic[2]=1

print(div(N))

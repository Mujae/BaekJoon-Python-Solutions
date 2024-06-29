import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

def div(n):
    if n<=2:
        return dic[n]
    elif dic[n]>0:#값이 있으면 사용
        return dic[n]
    else:#값이 없는 경우 F_2n-1 = Fn^2 + F_n-1^2, F_2n = Fn(2F_n-1 + Fn)을 활용
        h=n//2
        if n%2==0:
            dic[n]=(2*div(h-1)*div(h) + div(h)**2)%1000000007
            return dic[n]
        else:
            dic[n]=(div(h+1)**2 + div(h)**2)%1000000007
            return dic[n]
    
dic = defaultdict(int)#값이 있냐 없냐 할 때 편하려고 int
dic[1]=1
dic[2]=1

print(div(N))

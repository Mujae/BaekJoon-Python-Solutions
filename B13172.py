import sys

input = sys.stdin.readline

M = int(input())

#지수를 계속 반으로 나눠줌 
def fast_pow(a, b):
    global MOD
    res = 1
    while b>0:
        if b%2 == 1:
            res = (res*a)%MOD
        a = (a*a)%MOD
        b = b//2
    return res

s = 0
MOD = 1000000007
while M>0:
    N, S = map(int, input().split())
    s+=S*fast_pow(N, MOD-2)%MOD#페르마의 소정리에 따른 MOD의 역원 구하기
    M-=1

print(s%MOD)

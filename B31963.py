import sys
import math

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
combo =[0]*N
c=0
for i in range(1,N):#값이 커졌을 때를 고려하는게 point
    combo[i]=max(0,int(math.ceil(math.log2(float(A[i-1])/float(A[i]))+combo[i-1])))
    c+=combo[i]
print(c)

import sys

input = sys.stdin.readline
#최장 공통 부분 문자열 찾기 
s1 = input().rstrip()#문자1
s2 = input().rstrip()#문자2

l1 = len(s1)
l2 = len(s2)

li = [[0]*(l2+1) for _ in range(l1+1)]
m = 0

for i in range(1,l1+1):
    for j in range(1,l2+1):
        if s1[i-1]==s2[j-1]:
            li[i][j]=li[i-1][j-1]+1
            m=max(m,li[i][j])

print(m)

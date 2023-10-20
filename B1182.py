import sys

input = sys.stdin.readline

n, s = map(int, input().split())
li = list(map(int, input().split()))
c=0
st=[]
def go(m,k):
    global n, s, c
    if m>=n:
        return
    if k+li[m]==s:
        c+=1
    go(m+1,k)
    go(m+1,k+li[m])

go(0,0)
print(c)

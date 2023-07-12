# 모든 곳을 들려야 -> 다 방문은 아니지만 처음 그곳이면 그냥 탈
import sys

def go(o, ct):
    global start, y
    if o==start and ct>0:
        if len(st)==n:
            y= min(y,ct)
            li2.append(ct)
        return
    for k in range(n):
        if li[o][k]>0:#visited x -> 
            if  k not in st:
                st.append(k)
                go(k,ct+li[o][k])
                st.pop()

input = sys.stdin.readline
n = int(input())
li=[]

#스택에 현재 들른 곳을 저장할 것
for _ in range(n):
    li.append(list(map(int, input().split())))
st=[]# stack
start=0
li2=[]
y=1000000000
go(0, 0)
print(y)

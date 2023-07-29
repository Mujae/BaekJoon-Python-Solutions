import sys
input = sys.stdin.readline

n = int(input())

li=[]#값 저장 리스트

li2=[]#명령
for _ in range(n):
    li2.append(list(map(int, input().split())))
stack=[]
def dfs(a):
    global li, li2,stack,n
    if a==n:
        li.append(sum(stack))
        return
    c=0
    for i in range(a,n):
        if i+li2[i][0]-1<n:
            c+=1
            stack.append(li2[i][1])
            dfs(i+li2[i][0])
            stack.pop()
    if c==0:
        li.append(sum(stack))
        return
dfs(0)
print(max(li))

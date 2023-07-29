'''
import sys
l=0
def go(o):
    global l, stack, li
    if len(stack)==6:
        print(*stack)
        return
    for j in range(o,l):
        if li[j] not in stack:
            stack.append(li[j])
            go(j)
            stack.pop()
            
input = sys.stdin.readline
stack=[]
li=[]
while True:
    li=list(map(int, input().split()))
    if li[0]==0:
        break
    l = li[0]+1
    for i in range(1,l-5):
        stack.append(li[i])
        go(i)
        stack.pop()
    print()
'''

def f(n):
    if n<2:
        return 1
    return n*f(n-1)
a=int(input())
print(f(a))

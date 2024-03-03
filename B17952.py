<<<<<<< HEAD
import sys

input = sys.stdin.readline

n = int(input())
li=[]
s=0
for i in range(n):
    a = list(map(int, input().split()))
    if len(a)==1:
        if li:
            if li[-1][2]==1:
                s+=li[-1][1]
                li.pop()
            else:
                li[-1][2]-=1
    else:
        li.append(a)
        li[-1][2]-=1
        if li[-1][2]==0:
            s+=li[-1][1]
            li.pop()
print(s)
        
=======
import sys

input = sys.stdin.readline

n = int(input())
li=[]
s=0
for i in range(n):
    a = list(map(int, input().split()))
    if len(a)==1:
        if li:
            if li[-1][2]==1:
                s+=li[-1][1]
                li.pop()
            else:
                li[-1][2]-=1
    else:
        li.append(a)
        li[-1][2]-=1
        if li[-1][2]==0:
            s+=li[-1][1]
            li.pop()
print(s)
        
>>>>>>> d7c56fca9a24f348cba30b7014bd3a6f493c063d

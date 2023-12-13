import sys

input = sys.stdin.readline

n = int(input())

li1 = {}

for i in range(n):
    a, b= input().split()
    li1[a]=b
    
li1= dict(sorted(li1.items(), key=lambda x: x[0], reverse=True))

for i,j in li1.items():
    if j=='enter':
        print(i)

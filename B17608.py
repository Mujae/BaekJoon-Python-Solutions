import sys

input = sys.stdin.readline

n = int(input())

li=[0]

for i in range(n):
    a = int(input())
    if li[-1]<a:
        while li:
            if li[-1]>a:
                break
            li.pop()
    li.append(a)

print(len(li))

import sys

N = int(sys.stdin.readline().strip()) 
heights = [int(sys.stdin.readline().strip()) for _ in range(N)]

count = 1 
max_height = heights[-1] 

for i in range(N - 2, -1, -1): 
    if heights[i] > max_height:
        count += 1
        max_height = heights[i]  

print(count)

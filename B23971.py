import sys
import math

input = sys.stdin.readline

h, w, n, m = map(int,input().split())

li=[[0]*w for _ in range(h)]
c=0

for i in range(h):
    for j in range(w):
        if li[i][j]==0:
            c+=1
            for k in range(n+1):
                for q in range(m+1):
                    if i+k<h and j+q<w:
                        li[i+k][j+q]=1

print(c)
            

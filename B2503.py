import sys

input = sys.stdin.readline
n = int(input())
li=[]
for _ in range(n):
    li.append(list(map(int, input().split())))
t=0

for i in range(1,10):
    for j in range(1,10):
        if i==j:
            continue
        for k in range(1,10):
            if i==k or j==k:
                continue
            l = len(li)
            o=0
            for w in range(l):
                a,b,c = li[w]

                s=str(a)
                y=0
                if s[0]==str(i):
                    y+=1
                if s[1]==str(j):
                    y+=1
                if s[2]==str(k):
                    y+=1
                if y!=b:
                    o=1
                    break
                y=0
                if int(s[0]) in (i, j, k):
                    y+=1
                if int(s[1]) in (i, j, k):
                    y+=1
                if int(s[2]) in (i, j, k):
                    y+=1
                if y-b!=c:
                    o=1
                    break
            if o==0:
                t+=1
print(t)
                        
                
                
            

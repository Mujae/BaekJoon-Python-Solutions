import sys

input = sys.stdin.readline


m = []

for _ in range(19):
    m.append(list(map(int, input().split())))

x, y =0, 0
w=0
for i in range(19):
    for j in range(19):
        if m[i][j]==1:
            c=0
            for k in range(1,6):
                if j+k>18 or i-k<0:
                    break
                if m[i-k][j+k]==1:
                    c+=1
                else:
                    break
            for k in range(6):
                if j-k<0 or i+k>18:
                    break
                if m[i+k][j-k]==1:
                    x=i+k
                    y=j-k
                    c+=1
                else:
                    break
            if c==5:
                w=1
                break
            c=0
            for k in range(6):
                if j+k>18:
                    break
                if m[i][j+k]==1:
                    c+=1
                else:
                    break
            for k in range(1,6):
                if j-k<0:
                    break
                if m[i][j-k]==1:
                    x=i
                    y=j-k
                    c+=1
                else:
                    break
            if c==5:
                w=1
                break
            c=0
            for k in range(1,6):
                if i+k>18:
                    break
                if m[i+k][j]==1:
                    c+=1
                else:
                    break
            for k in range(6):
                if i-k<0:
                    break
                if m[i-k][j]==1:
                    x=i-k
                    y=j
                    c+=1
                else:
                    break
            if c==5:
                w=1
                break
            c=0
            for k in range(1,6):
                if j+k>18 or i+k>18:
                    break
                if m[i+k][j+k]==1:
                    c+=1
                else:
                    break
            for k in range(6):
                if j-k<0 or i-k<0:
                    break
                if m[i-k][j-k]==1:
                    x=i-k
                    y=j-k
                    c+=1
                else:
                    break
            if c==5:
                w=1
                break
        elif m[i][j]==2:
            c=0
            for k in range(1,6):
                if j+k>18 or i-k<0:
                    break
                if m[i-k][j+k]==2:
                    c+=1
                else:
                    break
            for k in range(6):
                if j-k<0 or i+k>18:
                    break
                if m[i+k][j-k]==2:
                    x=i+k
                    y=j-k
                    c+=1
                else:
                    break
            if c==5:
                w=2
                break
            c=0
            for k in range(1,6):
                if j+k>18:
                    break
                if m[i][j+k]==2:
                    c+=1
                else:
                    break
            for k in range(6):
                if j-k<0:
                    break
                if m[i][j-k]==2:
                    x=i
                    y=j-k
                    c+=1
                else:
                    break
            if c==5:
                w=2
                break
            c=0
            for k in range(1,6):
                if i+k>18:
                    break
                if m[i+k][j]==2:
                    c+=1
                else:
                    break
            for k in range(6):
                if i-k<0:
                    break
                if m[i-k][j]==2:
                    x=i-k
                    y=j
                    c+=1
                else:
                    break
            if c==5:
                w=2
                break
            c=0
            for k in range(1,6):
                if j+k>18 or i+k>18:
                    break
                if m[i+k][j+k]==2:
                    c+=1
                else:
                    break
            for k in range(6):
                if j-k<0 or i-k<0:
                    break
                if m[i-k][j-k]==2:
                    x=i-k
                    y=j-k
                    c+=1
                else:
                    break
            if c==5:
                w=2
                break
    if w>0:
            break


print(w)
if w!=0:
    print(x+1, y+1)

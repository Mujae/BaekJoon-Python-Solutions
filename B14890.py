import sys
input = sys.stdin.readline

n, l = map(int, input().split())
li=[]

for _ in range(n):
    li.append(list(map(int, input().split())))

#그냥 가로 n번, 세로 n번 ㄱㄱ
count=0
for i in range(n):#가로부터 ㄱㄱ
    s=li[i][0]
    c=1
    ud=1
    for j in range(1,n):
        if ud==1:
            if j==n-1:
                if s==li[i][j]:
                    
                    count+=1
                else:
                    if s-li[i][j]==-1:
                        if c>=l:
                          
                            count+=1
                    elif s-li[i][j]==1:
                        if l==1:
                            count+=1
                break
            if s!=li[i][j]:
                if s-li[i][j]==-1:
                    if c>=l:
                        c=1
                        s=li[i][j]
                    else:
                        break
                elif s-li[i][j]==1:
                    ud=0
                    c=1
                    s=li[i][j]
                    
                else:
                    break
            else:
                c+=1
        else:
            if j==n-1:
                if s==li[i][j]:
                    c+=1
                    if c>=l:
                      
                        count+=1
                elif s-li[i][j]==-1:
                    if c>=2*l:
                      
                        count+=1
                elif s-li[i][j]==1:
                    if l==1:
                       
                        count+=1
                break
            if s!=li[i][j]:
                if s-li[i][j]==-1:
                    if c>=2*l:
                        c=1
                        s=li[i][j]
                        ud=1
                    else:
                        break
                elif s-li[i][j]==1:
                    if c>=l:
                        c=1
                        s=li[j][i]
                    else:
                        break
                else:
                    break
            else:
                c+=1
for i in range(n):#세
    s=li[0][i]
    c=1
    ud=1
    for j in range(1,n):
        if ud==1:
            if j==n-1:
                if s==li[j][i]:
                  
                    count+=1
                else:
                    if s-li[j][i]==-1:
                        if c>=l:
                         
                            count+=1
                    elif s-li[j][i]==1:
                        if l==1:
                            count+=1
                break
            if s!=li[j][i]:
                if s-li[j][i]==-1:
                    if c>=l:
                        c=1
                        s=li[j][i]
                    else:
                        break
                elif s-li[j][i]==1:
                    ud=0
                    c=1
                    s=li[j][i]
                    
                else:
                    break
            else:
                c+=1
        else:
            if j==n-1:
                if s==li[j][i]:
                    c+=1
                    if c>=l:
                        
                        count+=1
                elif s-li[j][i]==-1:
                    if c>=2*l:
                      
                        count+=1
                elif s-li[j][i]==1:
                    if l==1:
                        count+=1
                break
            if s!=li[j][i]:
                if s-li[j][i]==-1:
                    if c>=2*l:
                        c=1
                        s=li[j][i]
                        ud=1
                    else:
                        break
                elif s-li[j][i]==1:
                    if c>=l:
                        c=1
                        s=li[j][i]
                        ud=0
                    else:
                        break
                else:
                    break
            else:
                c+=1

print(count)

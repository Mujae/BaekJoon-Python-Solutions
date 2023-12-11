import sys

#1은 소수가 아니라는걸 깜빡s ㅎㅎ;
input = sys.stdin.readline

m = int(input())
n = int(input())

li=[]#소수저장

for i in range(m, n+1):
    c=0
    if i<6:
        if i!=4 and i!=1:
            li.append(i)
    else:
        for j in range(2,i//2):
            if i%j==0:
                c+=1
                break
        if c==0:
            li.append(i)
if len(li)>0:
    print(sum(li))
    print(li[0])
else:
    print(-1)

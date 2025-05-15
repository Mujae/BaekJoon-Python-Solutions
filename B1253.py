N = int(input())
li = sorted(list(map(int, input().split())))
if N<3:
    print(0)
else:
    c=0
    for k in range(N):
        i = 0
        j = N-1
        while i!=j:
            if j==k:
                j-=1
            elif i==k:
                i+=1
            if j==i or i<0 or j>N-1:
                break
            s = li[i]+li[j]
            if s==li[k]:
                c+=1
                break
            elif s>li[k]:
                j-=1
            elif s<li[k]:
                i+=1
               
    print(c)

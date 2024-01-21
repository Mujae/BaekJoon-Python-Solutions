import sys

input = sys.stdin.readline

#산성 1~1000,000,000 알칼리는 반대 -

n = int(input())

li = list(map(int, input().split()))

start=0
end = n-1
m=1000000000
i, j= 0, 0
while start!=end:
    s = li[start]+li[end]
    if s>0:
        if s<m:
            m=s
            i=start
            j=end
        end-=1
    elif s<0:
        if s>m:
            m=-s
            i=start
            j=end
        start+=1
    else:
        print(li[start], li[end])
        exit()
print(li[i], li[j])

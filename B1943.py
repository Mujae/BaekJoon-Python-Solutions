import sys

input = sys.stdin.readline

for _ in range(3):
    N = int(input())

    li=[]

    for i in range(N):
        won, c = map(int, input().split())
        for j in range(c):
            li.append(won)
    li = sorted(li)

    l = sum(li)

    if l%2==1:
        print(0)
        continue

    l = l//2
    check = 0

    dp = [[0]*(len(li)) for _ in range(l+1)]
    
    for i in range(len(li)):
        for j in range(1, l+1):
            if i==0:
                if j==li[i]:
                    dp[j][i]=li[i]
                else:
                    dp[j][i]=dp[j-1][i]
    
            else:
                if j>li[i]:
                    dp[j][i] = max(dp[j][i-1],dp[j-li[i]][i-1]+li[i])
                else:
                    dp[j][i] = max(dp[j][i-1],dp[j-1][i])
    
    for i in range(len(li)):
        if dp[-1][i]==l:
            check=1

    print(check)

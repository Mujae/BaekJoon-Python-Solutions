n = int(input())

dp = [0] * (n + 1)

if n==1:
    print(1)
elif n==2:
    print(2)
elif n==3:
    print(2)
else:
    dp[1]=1
    dp[2]=2
    dp[3]=2
    for i in range(4,n+1):
        if i%2==0:
            dp[i]=(dp[i-1]+dp[i//2])%1000000000
        else:
            dp[i]=dp[i-1]
    print(dp[n])


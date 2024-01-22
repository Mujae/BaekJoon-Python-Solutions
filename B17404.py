import sys

input=sys.stdin.readline

INF = 1000000
N = int(input())
li = []
ans = INF
for _ in range(N):
    li.append(list(map(int, input().split())))

for i in range(3):
    dp = [[INF, INF, INF] for _ in range(N)]
    dp[0][i] = li[0][i]
    for j in range(1, N):
        dp[j][0] = li[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = li[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = li[j][2] + min(dp[j-1][0], dp[j-1][1])
    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])
print(ans)

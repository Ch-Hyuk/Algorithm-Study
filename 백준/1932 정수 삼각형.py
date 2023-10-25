import sys

input = sys.stdin.readline

n = int(input())
dp = []

for _ in range(n):
    li = list(map(int,input().split()))
    dp.append(li)

for i in range(n):
    for j in range(i+1):
        if i == 0:
            continue

        if j-1 < 0:
            left = 0
            right = dp[i-1][j]

        elif j >= len(dp[i-1]):
            left = dp[i-1][j-1]
            right = 0

        else:
            left = dp[i-1][j-1]
            right = dp[i-1][j]

        dp[i][j] = max(left, right) + dp[i][j]

print(max(dp[-1]))
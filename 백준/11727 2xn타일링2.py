n = int(input())

dp = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[i] = 1
        continue

    if i%2 != 0:
        dp[i] = (dp[i-1]*2) + 1

    else:
        dp[i] = (dp[i-1]*2) - 1

print(dp)
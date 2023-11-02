def echin(N):
    if N <= 2:
        return dp[N-1]
    
    for i in range(3,N+1):
        dp.append(dp[i-2] + dp[i-3])

    return dp[-1]

dp = [1, 1]

print(echin(int(input())))
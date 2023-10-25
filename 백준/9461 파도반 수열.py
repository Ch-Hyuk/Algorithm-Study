import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    dp = [1,1,1,2,2]
    N = int(input())
    if N <= 5:
        print(dp[N-1])
        continue

    idx = 0
    cnt = 5
    while dp:
        if cnt == N:
            print(dp[-1])
            break
            
        dp.append(dp[-1]+dp[idx])
        idx += 1
        cnt += 1
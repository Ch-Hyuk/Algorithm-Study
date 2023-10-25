import sys

input = sys.stdin.readline

stairs = int(input())
stairs_score = []
dp = [0 for _ in range(stairs)]

for _ in range(stairs):
    stairs_score.append(int(input()))

if stairs <= 2:
    print(sum(stairs_score))
    exit()

dp[0] = stairs_score[0]
dp[1] = stairs_score[0]+stairs_score[1]
dp[2] = max(stairs_score[0]+stairs_score[2], stairs_score[1]+stairs_score[2])

if stairs == 3:
    print(dp[2])

else:
    for i in range(3, stairs):
        dp[i] = max(dp[i-2], dp[i-3]+stairs_score[i-1]) + stairs_score[i]

    print(dp[-1])
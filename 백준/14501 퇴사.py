import sys

input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(N+1)]
board = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(i+board[i][0], N+1):
        if dp[j] < dp[i] + board[i][1]:
            dp[j] = dp[i] + board[i][1]

print(dp[-1])
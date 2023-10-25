import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int,input().split()))
dp = [0 for _ in range(len(num_list))]

for i in range(len(num_list)):
    if i == 0:
        dp[0] = num_list[0]
        continue

    if dp[i-1] < 0:
        dp[i] = num_list[i]
    else:
        dp[i] = dp[i-1] + num_list[i]

print(dp)

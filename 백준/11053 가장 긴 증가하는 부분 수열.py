import sys

input = sys.stdin.readline

A = int(input())

A_list = list(map(int,input().split()))
dp = [1 for _ in range(A)]

for i in range(A):
    for j in range(i):
        if A_list[i] > A_list[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
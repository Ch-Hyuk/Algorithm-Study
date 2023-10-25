import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    people_num = [1*i for i in range(1,n+1)]

    for _ in range(k):
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = sum(people_num[:i+1])

        people_num = dp

    print(people_num[-1])
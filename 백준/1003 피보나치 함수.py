import sys

T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())
    if n == 1:
        print(0, 1)
        continue

    if n == 0:
        print(1, 0)
        continue

    zero_cnt = [0 for _ in range(n+1)]
    one_cnt = [0 for _ in range(n+1)]

    zero_cnt[0] = 1
    one_cnt[1] = 1

    for i in range(2,n+1):
        zero_cnt[i] = zero_cnt[i-1] + zero_cnt[i-2]
        one_cnt[i] = one_cnt[i-1] + one_cnt[i-2]

    print(zero_cnt[-1], one_cnt[-1])
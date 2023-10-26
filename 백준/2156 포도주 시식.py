#계단오르기와 비슷한 개념으로 접근 
#다른점: 계단오르기는 중간 계단을 무조건 밟아야함 -> 포도주는 얼마든지 건너뛰기가 가능
#        계단오르기는 마지막 계단을 무조건 밟아야함 -> 포도주는 그런 개념이 없음
#값 저장 list = li
# -> dp[i] = max(max(dp[i-2] + li[i], dp[i-3] + li[i-1] + li[i]), dp[i-1])
# 이전 index의 dp list와의 비교도 진행해 주어야 함

import sys

input = sys.stdin.readline

wine = int(input())
wine_amount = []
dp = [0 for _ in range(wine)]

for _ in range(wine):
    wine_amount.append(int(input()))

if wine <= 2:
    print(sum(wine_amount))
    exit()

dp[0] = wine_amount[0]
dp[1] = wine_amount[0]+wine_amount[1]
dp[2] = max(max(wine_amount[0]+wine_amount[2], wine_amount[1]+wine_amount[2]),dp[1])

for i in range(3, wine):
    dp[i] = max(max(dp[i-2], dp[i-3]+wine_amount[i-1]) + wine_amount[i], dp[i-1])

print(max(dp))
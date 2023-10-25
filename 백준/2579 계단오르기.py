import sys

input = sys.stdin.readline

stairs = int(input())
stairs_score = [0]

def dfs(n, score, b):
    if n < stairs:
        return

    if n == 0:
        dfs(n+1, stairs_score[n],False)
        dfs(n+2, stairs_score[n],True)
        return

    if b:
        if n == stairs:
            b_max[stairs] = max(b_max[stairs], score + stairs_score[-1])
            return
        
        

    else:
        if n == stairs:
            a_max[stairs] = max(b_max[stairs], score + stairs_score[-1])
            return




        stairs_score[n]

#a -> 다음 계단을 밟을 수 있는 상태의 각 계단에서의 최대값: +1이 가능
#b -> 다음 계단을 밟을 수 없는 상태의 각 계단에서의 최대값: +2가 불가능
a_max = [0 for _ in range(stairs+1)]
b_max = [0 for _ in range(stairs+1)]
max_li = []

for _ in range(stairs):
    stairs_score.append(int(input()))

dfs(0, 0, True)
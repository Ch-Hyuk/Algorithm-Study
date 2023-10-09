import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int,input().split())

board = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for num in range(N):
    board[num] = list(map(int,input().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_value = 0

def dfs(row, col, total_sum, cnt):
    global max_value

    if cnt == 4:
        max_value = max(max_value, total_sum)
        return
    
    for d in range(4):
        dr = row + dx[d]
        dc = col + dy[d]

        if dr < 0 or dc < 0 or dr >= N or dc >= M or visited[dr][dc] == 1:
            continue
        
        visited[dr][dc] = 1
        dfs(dr, dc, total_sum+board[dr][dc], cnt+1)
        visited[dr][dc] = 0

def ex_process(row, col, num):
    global max_value
    
    for idx in list(combinations([0,1,2,3], 3)):
        total_sum = num

        for d in idx:
            dr = row + dx[d]
            dc = col + dy[d]

            if dr < 0 or dc < 0 or dr >= N or dc >= M:
                break
            
            total_sum += board[dr][dc]

        max_value = max(max_value, total_sum)


for row in range(N):
    for col in range(M):
        visited[row][col] = 1
        dfs(row, col, board[row][col], 1)
        visited[row][col] = 0
        ex_process(row, col, board[row][col])

print(max_value)

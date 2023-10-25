import sys

input = sys.stdin.readline

N = int(input())

RGB = [list(map(int,input().split())) for _ in range(N)]
min_board = [[0]*3 for _ in range(N)]

for i in range(N):
    if i == 0:
        min_board[i][0] = RGB[i][0]
        min_board[i][1] = RGB[i][1]
        min_board[i][2] = RGB[i][2]

    else:
        min_board[i][0] = min(min_board[i-1][1], min_board[i-1][2]) + RGB[i][0]
        min_board[i][1] = min(min_board[i-1][0], min_board[i-1][2]) + RGB[i][1]
        min_board[i][2] = min(min_board[i-1][0], min_board[i-1][1]) + RGB[i][2]

print(min(min_board[-1]))
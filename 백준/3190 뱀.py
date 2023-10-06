import sys
from collections import deque

def move_direction(dir, idx):
    if dir =='D':
        idx -= 1
    else:
        idx += 1

    if idx < 0:
        return 3
    
    elif idx > 3:
        return 0
    
    else:
        return idx


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
present_time = 0
present_loc = [0,0]
present_mov = 0
present_dir = 0

N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]

for _ in range(K):
    row, col = map(int,sys.stdin.readline().split())
    board[row-1][col-1] = 2

L = int(input())
move_list = []

for _ in range(L):
    X, D = sys.stdin.readline().split()
    move_list.append([int(X), D])

bamm = deque([[0,0]])

while bamm:
    r, c = present_loc
    dr = r + dx[present_dir]
    dc = c + dy[present_dir]
    present_time += 1

    if dr < 0 or dc < 0 or dr >= N or dc >= N or [dr, dc] in bamm:
        print(present_time)
        break

    present_loc = [dr, dc]

    bamm.append(present_loc)

    if board[dr][dc] != 2:
        bamm.popleft()
    
    else:
        board[dr][dc] = 0
    
    if present_mov < len(move_list) and present_time == move_list[present_mov][0]:
        present_dir = move_direction(move_list[present_mov][1], present_dir)
        present_mov += 1

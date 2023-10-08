import sys
from collections import deque

input = sys.stdin.readline
N,M,x,y,k = map(int,input().split())

board = [[0]*M for _ in range(N)]

for num in range(N):
    board[num] = list(map(int,input().split()))

dir_comm = list(map(int,input().split()))

que1 = deque([0,0,0,0])
que2 = deque([0,0,0,0])

location = [x, y]

for num in dir_comm:
    if num == 1:
        r,c = location
        c += 1

        if c < 0 or c >= M:
            continue

        if board[r][c] == 0:
            que2.rotate(-1)
            que1[1] = que2[1]
            que1[3] = que2[3]
            board[r][c] = que2[3]

        else:
            que2.rotate(-1)
            que2[3] = board[r][c]
            board[r][c] = 0
            que1[1] = que2[1]
            que1[3] = que2[3]

    elif num == 2:
        r,c = location
        c -= 1

        if c < 0 or c >= M:
            continue

        if board[r][c] == 0:
            que2.rotate(1)
            que1[1] = que2[1]
            que1[3] = que2[3]
            board[r][c] = que2[3]

        else:
            que2.rotate(1)
            que2[3] = board[r][c]
            board[r][c] = 0
            que1[1] = que2[1]
            que1[3] = que2[3]

    elif num == 3:
        r,c = location
        r -= 1

        if r < 0 or r >= N:
            continue

        if board[r][c] == 0:
            que1.rotate(1)
            que2[1] = que1[1]
            que2[3] = que1[3]
            board[r][c] = que1[3]

        else:
            que1.rotate(1)
            que1[3] = board[r][c]
            board[r][c] = 0
            que2[1] = que1[1]
            que2[3] = que1[3]

    else:
        r,c = location
        r += 1

        if r < 0 or r >= N:
            continue

        if board[r][c] == 0:
            que1.rotate(-1)
            que2[1] = que1[1]
            que2[3] = que1[3]
            board[r][c] = que1[3]

        else:
            que1.rotate(-1)
            que1[3] = board[r][c]
            board[r][c] = 0
            que2[1] = que1[1]
            que2[3] = que1[3]

    location = [r, c]
    print(que1[1])
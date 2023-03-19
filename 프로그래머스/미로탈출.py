from collections import deque

def solution(maps):
    answer = 0
    max_row, max_col = len(maps), len(maps[0])
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    start,lever = (),()
    for i in range(max_row):
        for j in range(max_col):
            if maps[i][j] == 'S':
                start = (i, j, 0)
            if maps[i][j] == 'L':
                lever = (i, j)

    visited = set()
    visited.add((start[0],start[1]))
    que = deque([start])
    lever_on = False
    while que:
        if lever_on == True:
            break

        row, col, dis = que.popleft()
        for d in range(4):
            dr = row + dx[d]
            dc = col + dy[d]

            if dr < 0 or dc < 0 or dr > max_row-1 or dc > max_col-1 or maps[dr][dc] == 'X' or (dr,dc) in visited:
                continue

            if maps[dr][dc] == 'O' or maps[dr][dc] == 'E':
                visited.add((dr,dc))
                que.append((dr,dc,dis+1))

            if maps[dr][dc] == 'L':
                lever_on = True
                answer += dis +1
                break

    if answer == 0:
        return -1

    que = deque([(lever[0],lever[1],answer)])
    visited = {lever}
    while que:

        row, col, dis = que.popleft()
        for d in range(4):
            dr = row + dx[d]
            dc = col + dy[d]

            if dr < 0 or dc < 0 or dr > max_row-1 or dc > max_col-1 or maps[dr][dc] == 'X' or (dr,dc) in visited:
                continue

            if maps[dr][dc] == 'O' or maps[dr][dc] == 'S':
                visited.add((dr,dc))
                que.append((dr,dc,dis+1))

            if maps[dr][dc] == 'E':
                return dis+1

    return -1
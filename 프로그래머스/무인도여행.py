from collections import deque

def bfs(row,col):
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    que = deque([(row,col)])
    island = int(maps[row][col])
    maps[row][col] = 'X'
    while que:
        row, col = que.popleft()
        
        for d in range(4):
            nr = row + dx[d]
            nc = col + dy[d]

            if nr < 0 or nc < 0 or nr >= len(maps) or nc >= len(maps[0]) or maps[nr][nc] == 'X':
                continue

            if maps[nr][nc] != 'X':
                que.append((nr,nc))
                island += int(maps[nr][nc])
                maps[nr][nc] = 'X'

    return island
        

def solution(maps):
    answer = []

    for idx in range(len(maps)):
        maps[idx] = list(maps[idx])

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'X':
                continue
            
            answer.append(bfs(i,j))
    
    return sorted(answer)

maps = ["X591X","X1X5X","X231X", "1XXX1"]
print(solution(maps))
import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
N, L, R = map(int, input().split())
A = list()

for i in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))

def bfs(row, column):
    union = [(row,column)]
    visited[row][column] = 1
    union_sum = A[row][column]
    que = deque([(row, column)])
    cnt = 1
    while que:
        r, c  = que.popleft()
        for d in range(4):
            nr = r + dx[d]
            nc = c + dy[d]

            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue

            if visited[nr][nc] == 1:
                continue
        
            if L <= abs(A[r][c] - A[nr][nc]) <= R:
                visited[nr][nc] = 1
                que.append((nr,nc))
                union.append((nr,nc))
                cnt += 1
                union_sum += A[nr][nc]

    
    for x, y in union:
        A[x][y] = union_sum//cnt

    print(A)
    return cnt

answer = 0

while True:
    visited = [[0] * N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                continue
            else:
                if bfs(i, j) > 2:
                    flag = 1

    if flag == 1:
        answer += 1
    else:
        print(answer)
        break
from collections import deque

N,M = map(int,input().split())
visited = {(0,0,0)}
board = [input() for _ in range(N)]
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

que = deque([(0,0,0,1)])

def bfs():
        que = deque([(0,0,0,1)])
        while que:
                row, col, wall, dis = que.popleft()
                if row == N-1 and col == M-1:
                        return dis
                for d in range(4):
                        dr = row +dx[d]
                        dc = col +dy[d]

                        if dr < 0 or dc <0 or dr >= N or dc >= M or (dr, dc, wall) in visited:
                                continue
                
                        if board[dr][dc] == '0':
                                que.append((dr,dc,wall,dis+1))
                                visited.add((dr,dc,wall))
                        if board[dr][dc] == '1' and wall == 0:
                                que.append((dr,dc,wall+1,dis+1))
                                visited.add((dr,dc,wall+1))
        return -1

print(bfs())
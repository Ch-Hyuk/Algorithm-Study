from collections import deque

def solution(board):
    answer = 0
    start = []
    visited_cnt = [[0 for j in range(len(board[0]))] for i in range(len(board))]
    visited = set()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start = [i, j]
    
    que = deque([(start[0],start[1],-1,0)])
    while que:
        print(que)
        row, col, direction, cnt = que.popleft()
        
        for i in range(4):
            print(i, direction)
            if direction != -1 and direction != i:
                continue
            
            dr = row + dx[i]
            dc = col + dy[i]
            print(dr,dc)
            if dr >= len(board) or dr < 0 or dc >=len(board[0]) or dc < 0 or (dr,dc) in visited:
                continue  
            
            if dr == 0 or dc == 0 or dr == len(board)-1 or dc == len(board[0])-1:
                if board[dr][dc] == 'G':
                    return cnt+1
                visited_cnt[dr][dc] = cnt+1
                visited.add((dr,dc))
                que.append((dr,dc,-1,cnt+1))
            
            if board[dr][dc] == 'D':
                if board[row][col] == 'G':
                    return cnt+1
                visited_cnt[dr][dc] = cnt+1
                visited.add((row,col))
                que.append((row,col,-1,cnt+1))
                
            if direction == i:
                que.append((dr,dc,i,cnt))            
    return answer



solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])


from collections import deque

def solution(places):
    answer = [1, 1, 1, 1, 1]
    for p in range(5):
        i = 0

        while i < 5:
            for j in range(5):
                if places[p][i][j] == "P":
                    if bfs(i, j, places[p]) == 0:
                        answer[p] -= 1
                        i+=5
                        break

            i += 1

    return answer

def bfs(row, col, place):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    que = deque([(row, col)])
    des = [[0] * 5 for _ in range(5)]
    visited = [[0] * 5 for _ in range(5)]
    visited[row][col] = 1
    while que:
        r, c = que.popleft()
        for d in range(4):
            dr = r + dx[d]
            dc = c + dy[d]
            print(dr, dc)
            if dr < 0 or dc <0 or dr > 4 or dc > 4 or visited[dr][dc] != 0 or place[dr][dc] == "X":
                continue

            if place[dr][dc] == "O":
                que.append((dr,dc))
                des[dr][dc] = des[r][c] +1
                visited[dr][dc] = 1

            if place[dr][dc] == "P":
                des[dr][dc] = des[r][c] +1
                if des[dr][dc] <= 2:
                    return 0 
                
    return 1

place =[["POOPO", 
         "OOPOO", 
         "OPOOO", 
         "OOOPO", 
         "POOOO"],
        ["POXXX",
         "XPXXX", 
         "XXXXX", 
         "XXXXX", 
         "XXXXX"], 
        ["POOPO", 
         "OOPOO", 
         "OPOOO", 
         "OOOPO", 
         "POOOO"], 
        ["OOOOO", 
         "OXPOO", 
         "OPXOO", 
         "OOOOO", 
         "OOOOO"], 
        ["PXPOP", 
         "XPOOX", 
         "PXOOP", 
         "XPXPX", 
         "PXPXP"]]

print(solution(place))
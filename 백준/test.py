N,M = map(int,input().split())
wall = list()
visited = [["0"] * M for _ in range(N)]
distanced = [[0] * M for _ in range(N)]
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

for data in range(N):
    wall.append(input())

def dfs(i, j, wall_count, distance):
    cnt = wall_count
    dis = distance
    print("좌표:", i, j)
    print("cnt :", cnt)
    print(visited)
    if i < 0 or j <0 or i >= N or j >= M:
        print("out of range return")
        return

    if visited[i][j] == "X":
        print("X return")
        return

    if wall[i][j] == '1':
        if cnt == 1:
            visited[i][j] == "X"
            print(visited)
            print("wall return")
            return
        
        elif cnt == 0:
            visited[i][j] = "X"
            distanced[i][j] = dis
            cnt += 1

    if wall[i][j] == '0':
        visited[i][j] = "X"
        distanced[i][j] = dis

    for d in range(4):
        di = i +dx[d]
        dj = j +dy[d]
        dfs(di,dj,cnt, dis+1)


dfs(0,0,0,1)

print(distanced)
if distanced[N-1][M-1] == 1 or N==1 and M ==1 :
    print(-1)
else:
    print(distanced[N-1][M-1])
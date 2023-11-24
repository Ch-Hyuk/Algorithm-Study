from collections import deque
from copy import deepcopy

def solution(land):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n, m = len(land), len(land[0])
    group_cnt = {0:0}
    group = 1
    answer = []
    vis_land = deepcopy(land)

    for col in range(m):
        for row in range(n):
            cnt = 0
            if vis_land[row][col] == 0:
                continue

            group_cnt[group] = 0
            vis_land[row][col] = 0
            land[row][col] = group
            cnt += 1
            que = deque([[row, col]])

            while que:
                r, c = que.popleft()
                
                for d in range(4):
                    dr = r + dx[d]
                    dc = c + dy[d]
                    
                    if dr < 0 or dc < 0 or dr >= n or dc >= m or vis_land[dr][dc] == 0:
                        continue
                        
                    if vis_land[dr][dc] == 1:
                        cnt += 1
                        vis_land[dr][dc] = 0
                        land[dr][dc] = group

                        que.append([dr, dc])

            group_cnt[group] += cnt
            group += 1
            
    land = list(map(list, zip(*land)))
    
    for data in land:
        cnt = sum(group_cnt[key] for key in set(data))
        answer.append(cnt)

    return max(answer)

print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))
print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))
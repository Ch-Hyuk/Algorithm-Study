from collections import deque

N, K = map(int, input().split())

visited = [0]*100001

que = deque([N])

while que:
    num = que.popleft()
    if num == K:
        print(visited[num])
        break

    for n in [num-1, num+1, num*2]:
        if n < 0 or n > 100000 or visited[n] != 0:
            continue

        visited[n] = visited[num] + 1
        que.append(n)
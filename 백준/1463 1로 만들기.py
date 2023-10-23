from collections import deque

N = int(input())

visited = set()

que = deque([[N,1]])
flag = True

while flag:
    N, cnt = que.popleft()
    cal = [N-1]
    if N == 1:
        print(0)
        break

    if N%2 == 0:
        cal.append(N//2)
    
    if N%3 == 0:
        cal.append(N//3)

    for n in cal:
        if n in visited:
            continue

        if n == 1:
            print(cnt)
            flag = False
            break

        que.append([n,cnt+1])
        visited.add(n)
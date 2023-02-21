from collections import deque

def solution(x,y,n):
    if x == y:
        return 0

    visited = set()
    cal_li = [n,2,3]
    que = deque([(x,y,1)])
    while que:
        start, result, cnt = que.popleft()
        for c in range(3):
            if c == 0:cx = start + cal_li[c]
            else:cx = start * cal_li[c]

            if cx > y or cx in visited:
                continue

            if cx == y:
                return cnt

            visited.add(cx)
            que.append((cx,y,cnt+1))   

    return -1
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    que = deque()
    if cacheSize == 0:
        return len(cities)*5
    for i in cities:
        i = i.lower()
        if i in que:
            que.remove(i)
            que.append(i)
            answer += 1

        elif len(que) != 0 and cacheSize == len(que):
            que.popleft()
            que.append(i)
            answer += 5

        else:
            que.append(i)
            answer += 5

    return answer
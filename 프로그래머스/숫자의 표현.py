from collections import deque

def solution(n):
    answer,sum,num = 0,1,2
    que = deque([1])
    while que:
        if sum > n:
            sum -= que.popleft()
        
        elif sum == n:
            answer += 1
            sum -= que.popleft()
            
        else:
            que.append(num)
            sum += num
            num += 1
   
    return answer

print(solution(15))
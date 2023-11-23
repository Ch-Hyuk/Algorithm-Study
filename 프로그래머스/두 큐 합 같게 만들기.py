# from collections import deque

# def solution(queue1, queue2):

#     que1,que2 = deque(queue1), deque(queue2)
#     qsum1,qsum2 = sum(que1), sum(que2)
#     answer = 0
    
#     while True:
#         if qsum1 == qsum2:
#             return answer
        
#         if qsum1 > qsum2:
#             data = que1.popleft()
#             que2.append(data)
#             qsum1 -= data
#             qsum2 += data
#             answer += 1
            
#         elif qsum2 > qsum1:
#             data = que2.popleft()
#             que1.append(data)
#             qsum2 -= data
#             qsum1 += data
#             answer += 1

def solution(queue1, queue2):
    total_que = queue1 + queue2
    que_sum = sum(queue1)

    if sum(total_que)%2 == 1:
        return -1
    
    target = sum(total_que)//2
    cnt = 0
    start, end = 0, len(queue1)-1

    while start < len(total_que) and end < len(total_que):
        print('que_sum: ',que_sum)
        if target == que_sum:
            return cnt
        
        if target > que_sum:
            end += 1
            que_sum += total_que[end]

        else:
            que_sum -= total_que[start]
            start += 1

        cnt += 1
    return -1

print(solution([1,1,1,1,1,1,1],[1,1,1,1,1,13,1]))

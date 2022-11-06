def solution(arr):
    answer = []
    for data in arr:
        answer.append(data)
        if len(answer) == 1:
            continue
        elif answer[-2] == answer[-1]:
            del answer[-1]
    
    return answer

arr = [1,1,3,3,0,1,1]
solution(arr)
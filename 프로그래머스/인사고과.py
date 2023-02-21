def solution(scores):
    answer = 1
    wanho = scores[0]
    scores.sort(key=lambda n: (-n[0], n[1]))
    max_score = 0
    for data in scores:
        if data[0] > wanho[0] and data[1] > wanho[1]:
            return -1
        
        if max_score <= data[1]:
            max_score = data[1]
            if sum(data) > sum(wanho):
                answer += 1
    
    return answer
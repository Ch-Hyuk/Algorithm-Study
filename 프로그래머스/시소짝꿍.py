from collections import Counter

def solution(weights):
    answer = 0
    ratio = [(2,3),(2,4),(3,4)]
    wei = Counter(weights)
    
    for data,num in wei.items():
        answer += num * (num-1) // 2
        for a, b in ratio:
            if data*a/b in wei.keys():
                answer += wei[data*a/b]*num

    return answer
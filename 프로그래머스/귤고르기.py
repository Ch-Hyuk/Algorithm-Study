from collections import Counter

def max_key(counter):
    max_cnt = -1
    for key in counter.keys():
        if counter[key] > max_cnt:
            max_cnt  = counter[key]
    return max_cnt, key

def solution(k, tangerine):
    answer = 0
    tang = sorted(Counter(tangerine).values())
    while(k > 0):
        k -= tang.pop()
        answer += 1
    return answer

tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
k = 6
print(solution(k, tangerine))
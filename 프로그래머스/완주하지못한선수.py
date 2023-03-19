def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(0, len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer

participant = ["mislav", "stanko", "mislav", "ana",'za']
completion = ["stanko", "ana", "mislav"]
print(solution(participant,completion))

print(participant + completion)


#collections 사용
from collections import Counter

def solution(participant, completion):
    return list((Counter(participant) - Counter(completion)).keys())[0]
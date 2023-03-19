#문자열 상태로 재할당 해주면 시초뜸

def solution(s):
    answer = []
    for i in s:
        answer.append(i)
        if len(answer) >= 2 and answer[-1] == answer[-2]:
            answer.pop()
            answer.pop()
    if len(answer) == 0:
        return 1
    else:
        return 0
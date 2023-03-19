def solution(n, m, section):
    answer,cnt = 1,1
    if m == 1:
        return len(section)

    for i in range(len(section)):
        length = abs(section[i] - section[i+1])+cnt
        answer += 1
        if m >= length:
            answer -= 1
            cnt = length

        elif m < length:
            cnt = 1

        if i+1 == len(section) - 1:
            return answer
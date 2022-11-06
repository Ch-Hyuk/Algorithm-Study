#문제를 똑바로 읽자 시발
def solution(survey, choices):
    dic ={
        "R": 0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0
    }
    answer = ''

    for idx in range(len(survey)):
        if choices[idx] < 4:
            dic[survey[idx][0]] += 4 - choices[idx]
        else:
            dic[survey[idx][1]] += choices[idx] - 4 

    answer += 'R' if dic['R'] >= dic['T'] else 'T'
    answer += 'C' if dic['C'] >= dic['F'] else 'F'
    answer += 'J' if dic['J'] >= dic['M'] else 'M'
    answer += 'A' if dic['A'] >= dic['N'] else 'N'

    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [1, 1, 1, 1, 1]

print(solution(survey, choices))

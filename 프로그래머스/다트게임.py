import re

sc_dic = {1:0,2:0,3:0}

def solution(dartResult):
    answer = 0 
    ch_dic = {1:"",2:"",3:""}
    cnt = 0
    for idx, data in enumerate(dartResult):
        print(idx, data, cnt)
        if 48 <= ord(data) <= 57:
            if idx == 0:
                cnt += 1
            elif dartResult[idx-1] != "1":
                cnt += 1
                
        ch_dic[cnt] = ch_dic[cnt] + data
        print(ch_dic)

    for chance, score in ch_dic.items():
        sc_dic[chance] = score_cal(chance, score)

    for i in sc_dic.values():
        answer += i

    return(answer)


def score_cal(num, str):
    score = 0
    if "S" in str:
        score = int(re.sub(r'[^0-9]','',str))
    elif "D" in str:
        score = int(re.sub(r'[^0-9]','',str))**2
    elif "T" in str:
        score = int(re.sub(r'[^0-9]','',str))**3

    if str[-1] == "*" or str[-1] == "#":
        if str[2] == "*":
            if num == 1:
                score*=2
            else:
                sc_dic[num-1] *= 2
                score*=2
        elif str[2] == "#":
            score*=(-1)

    return score



str = "1D2S#10S"
solution(str)
print(sc_dic)

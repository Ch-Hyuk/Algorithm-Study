def solution(name, yearning, photo):
    answer = []
    yearn_dic = {}
    
    for n, y in zip(name, yearning):
        yearn_dic[n] = y
    
    for i in photo:
        cnt = 0
        for j in i:
            if j in yearn_dic.keys():
                cnt += yearn_dic[j]
        answer.append(cnt)
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name, yearning, photo))
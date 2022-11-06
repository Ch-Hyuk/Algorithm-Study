def solution(N, stages):
    answer =[]
    dic ={}

    for stage in range(1, N+1):
        numer = 0
        denomi = 0
        #분자 확인
        if stage not in stages:
            dic[stage] = 0
            continue
        else:
            numer = stages.count(stage)

        #분모 확인
        for data in stages:
            if stage <= data:
                denomi += 1
        dic[stage] = numer/denomi
    
    sort_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for data in sort_dic:
        answer.append(data[0])
    
    return answer


stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 5

solution(N,stages)
from itertools import combinations_with_replacement

def solution(n, info):
    info = list(reversed(info))
    info_score = 0
    max = 0
    max_tu = tuple()
    answer = [0,0,0,0,0,0,0,0,0,0,0]
    score = [0,1,2,3,4,5,6,7,8,9,10]
    
    #어피치의 점수
    for idx, data in enumerate(info):
        if data != 0:
            info_score += idx
    
    for com_r in combinations_with_replacement(score, n):
        info_cnt = 0
        ryan_cnt = 0
        flag = True
        s_com_r = set(com_r)
        for data in s_com_r:
            #조건에 안맞는 조합들 제거
            if info[data] + 1 < com_r.count(data):
                flag = False
                continue
            
            #겹치는 점수 info_cnt 혹은 ryan_cnt 에 추가
            if info[data] != 0 and info[data] < com_r.count(data):
                info_cnt += data

            elif info[data] >= com_r.count(data):
                ryan_cnt += data
        
        #어피치가 이기는 경우 제거
        if info_score - info_cnt >= sum(s_com_r) - ryan_cnt:
            continue
            
        if flag == True and max < (sum(s_com_r) - ryan_cnt) - (info_score - info_cnt):
            max = sum(s_com_r) - (info_score - info_cnt)
            max_tu = com_r 
            
        #최댓값이 같은 것 중에서 점수가 낮은 것을 가지는 것 max_tu 추가
        if flag == True and max == (sum(s_com_r) - ryan_cnt) - (info_score - info_cnt):
            for i in score:
                if max_tu.count(i) < com_r.count(i):
                    max_tu = com_r
                    break

                elif max_tu.count(i) > com_r.count(i):  
                        break

    for score in max_tu:
        answer[score] += 1
    
    if len(max_tu) == 0:
        return [-1]
    else:
        return list(reversed(answer))

info = 	[0,0,0,0,0,0,0,0,3,4,3]
n = 10
print(solution(n, info))
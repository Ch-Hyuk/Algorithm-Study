#실패작
# def solution(id_list, report, k):
#     d_list = []
#     answer = []
#     re_report = list(set(report))
#     for id_l in id_list:
#         f_res = []
#         cnt=0
#         for re_l in re_report:
#             if re_l.endswith(id_l):
#                 print(re_l)
#                 f_res.append(re_l.replace(" "+id_l,""))
#                 cnt+=1
#         print(f_res)
#         if k <= cnt:
#             d_list.extend(f_res)

#     for id_l in id_list:
#         answer.append(d_list.count(id_l))
    
#     print(answer)
#     return answer


# id_list =["muzi", "frodo", "apeach", "neo","nimo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 5
# solution(id_list, report, k)

# li =["ryan con", "ryan con", "ryan con", "ryan con"]
# li = list(set(li))
# print(len(li))
# print(li)
# print(li[0].replace("ryan ", ""))
# print(li[0])

def solution(id_list, report, k):
    answer =[]
    dic = dict.fromkeys(id_list,0)
    re_report = list(set(report))
    report_1 = []
    report_2 = []
    for data in re_report:
        wspace = data.split(' ')
        report_1.append(wspace[0])
        report_2.append(wspace[1])
    
    print(report_1)
    print(report_2)
    cnt_dic={}
    for report_key in report_2:
        if report_key in cnt_dic:
            cnt_dic[report_key] += 1
        else:
            cnt_dic[report_key] = 1

    print(cnt_dic)
    for re in enumerate(report_2):
        print(re)
        if cnt_dic[re[1]] >= k:
            idx = re[0]
            print(idx)
            keys = report_1[idx]
            print(keys)
            dic[keys] = dic.get(keys)+1
            print('')

    print(dic)
    for id in id_list:
        answer.append(dic[id])
    return answer


id_list =["muzi", "frodo", "apeach", "neo","nimo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
solution(id_list, report, k)


#미친놈 코드
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

'''
answer는 id_list의 길이만큼 0으로 초기화한 list
reports는 id_list의 길이만큼 0으로 초기화한 딕셔너리
-첫 번째 for문 띄어쓰기를 기준으로 report를 돌리며 신고받은 횟수를 reports에 기록
-두 번째 for문 신고받은 횟수가 k이상이라면 그 문자열의 0번째 index 즉 신고한 사람의
id_list에서 index를 추출하여 결과값에 추가
'''


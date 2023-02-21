# # answer = 0
# # idx = 0
# # n = 15
# # sum_li = []
# # for i in range(n+1):
# #     if i == 0:
# #         sum_li.append(1)
# #     else:
# #         sum_li.append(sum_li[i-1]+i+1)

# #         if sum_li[i] == n:
# #             answer += 1

# #         if sum_li[i] > n and sum_li[i-1] <= n:
# #             idx = i

# # for i in range(idx, len(sum_li)):
# #     print(sum_li[i])
# #     if sum_li[i] > n:
# #         for j in range(0,idx):
# #             print(sum_li[j])
# #             if sum_li[i] - sum_li[j] < 0:
# #                 break

# #             if sum_li[i] - sum_li[j] == n:
# #                 print("?")
# #                 answer +=1
# #                 break
# #         idx += 1
# # print(answer)
# def solution(numbers, hand):
#     answer = ''
#     num_dic = {0:(3,1),1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2),'*':(3,0),'#':(3,2)}
#     L,R = '*', '#'
#     for pad in numbers:
#         L_dis = 0
#         R_dis = 0
#         if pad == 1 or pad == 4 or pad == 7:
#             L = pad
#             answer += 'L'
        
#         if pad == 3 or pad == 6 or pad == 9:
#             R = pad
#             answer += 'R'
            
#         if pad == 2 or pad == 5 or pad == 8 or pad == 0:
#             for p, l, r in zip(num_dic[pad],num_dic[L], num_dic[R]):
#                 L_dis += abs(p-l)
#                 R_dis += abs(p-r)

#             if L_dis < R_dis:
#                 L = pad
#                 answer += 'L'
                
#             elif L_dis > R_dis:
#                 R = pad
#                 answer += 'R'
            
#             else:
#                 if hand[0].upper() == 'L': L = pad
#                 elif hand[0].upper() == 'R': R = pad
#                 answer += hand[0].upper()
            
#     return answer

def solution(info, query):
    answer = []
    q_dic = {}

    for idx,data in enumerate(query):  
        data = data.replace(' and','')
        q_dic[idx] = data.split(' ')
    
    for que in q_dic:
        p_cnt = 0
        for data in info:
            cnt = 0
            for i in range(5):
                print(q_dic[que])
                if data.split()[i] == q_dic[que][i] or q_dic[que][i] == '-':
                    cnt += 1
                if i == 4:
                    if q_dic[que][i] == '-':
                        cnt += 1
                    elif int(data.split()[i]) >= int(q_dic[que][i]):
                        cnt += 1
            if cnt == 5:
                p_cnt += 1
        answer.append(p_cnt)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(info, query)
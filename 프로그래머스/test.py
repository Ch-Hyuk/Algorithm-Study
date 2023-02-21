# # import math

# # def solution(k, d):
# #     cen_point = d/2*math.sqrt(2)
# #     answer = (int(cen_point)//k+1)**2+2
# #     for i in range(0, d, k):

# #         if i <= cen_point:
# #             print(i)
# #             continue
# #         for j in range(0, int(cen_point)+1, k):
# #             if math.sqrt(i**2+j**2) <= d:
# #                 answer += 2
    
# #     return answer

# def solution(cards):
#     group = []
#     visited = set()
#     for i in range(1,len(cards)+1): 
#         cnt = 0
#         if cards[i-1] in visited:
#             continue
        
#         box = cards[i-1]
#         while box not in visited:
#             visited.add(box)
#             cnt+=1
#             box = cards[box-1]
            
#         group.append(cnt)
        
#     group.sort(reverse = True)    
    
#     return group[0] * group[1]

# cards = [2,1]
# print(solution(cards))

# from collections import defaultdict

# def solution(alp, cop, problems):
#     answer = 0
#     pos_problems = set()   #풀수 있는 문제 idx
#     # best_problems = [0,0]  #풀수 있는 문제중 alp 최대, cop 최대
#     dic_problems = defaultdict(list)
#     problems.sort(key=lambda x: (x[0],x[1]))
    
#     min_alp, min_cop = 200 ,200
#     max_alp,max_cop = -1, -1
#     for i in problems:
#         print(i)
#         dic_problems[i[4]].append(i)
#         print(dic_problems)
#         if i[0] <= alp and i[1] <= cop:
#             pos_problems.add(i)
        
#         if min_alp > i[0]:min_alp = i[0]
#         if min_alp > i[1]:min_alp = i[1]
#         if max_alp < i[0]:max_alp = i[0]           
#         if max_cop < i[1]:max_cop = i[1]
        
#     while True:
#         if alp >= max_alp and cop >= max_cop:
#             return answer
    
#         if alp < min_alp and cop < min_cop:
#             answer += (min_alp+min_cop)
#             pos_problems.add()
#             alp = min_alp
#             cop = min_cop

print(format(10, 'b').count('1'))
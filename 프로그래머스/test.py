from itertools import combinations
from collections import Counter
import math

# def solution(weights):
#     perms = list(combinations(weights, 2))
#     m_list = [1, 2, 3, 4]
#     answer = 0
#     for perm in perms:
#         if perm[0] == perm[1]:
#             answer += 1
#             continue

#         g = math.gcd(perm[0],perm[1])

#         if perm[0]//g in m_list and perm[1]//g in m_list:
#             answer+=1
            
#     return answer
# def rec(num, flag, idx):
#     if idx == len(num):
#         return 1

#     number = int(num[idx])

#     if number > 5:
#         answer = 10 - number - flag
#         flag = 1
#         return answer + rec(num, flag, idx+1) 

#     elif number == 5:
#         if flag == 5:



def solution(storey):
    answer = 0
    num_str = str(storey)[::-1]
    flag = 0
    for idx,num in enumerate(num_str):
        number = int(num)
        if number > 5:
            answer += 10-number -flag
            flag = 1

            if idx == len(num_str) -1:
                answer += 1

        elif number == 5:
            if idx == len(num_str) -1:
                return answer + 5

            if flag == 1:
                answer += 4
                flag = 1
            
            elif int(num_str[idx+1]) >= 5 :
                answer += 5
                flag = 1
            
            else:
                answer += 5
                flag = 0

        else:
            answer += number + flag
            flag = 0
        
    return answer


print(solution(55))
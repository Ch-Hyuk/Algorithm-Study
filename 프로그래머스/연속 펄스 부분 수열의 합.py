def solution(sequence):
    print(sequence)
    answer = []
    pulse= 1
    plus_pul_list = [0]
    sum_plus = [ 0 for _ in range(len(sequence)+1)]
    
    for i in sequence:
        plus_pul_list.append(i*pulse)
        pulse *= -1
    
    for i in range(1,len(plus_pul_list)):
        sum_plus[i] = sum_plus[i-1] + plus_pul_list[i]

    max_num = max(map(abs,sum_plus))
    max_idx = []
    for i,data in enumerate(sum_plus):
        if max_num == data or max_num == -data:
            max_idx.append(i)
    
    print(max_idx)
    print(plus_pul_list)
    print(sum_plus)
    for m in max_idx:
        for i in range(m-1, -1, -1):
            if (sum_plus[i] * sum_plus[m]) <= 0:
                print(sum_plus[m],sum_plus[i])
                if (plus_pul_list[i] * plus_pul_list[m]) > 0:
                    continue
                else:
                    answer.append(abs(sum_plus[m]-sum_plus[i]))
                    
                    #break
    print(answer)
    return max(answer)

    

li = [-1,2,8,-2,1,8,2,3,4,-2,4]
#li = [2, 3, -6, 1, 3, -1, 2, 4]
print(solution(li))

# def solution(sequence):
#     answer = 0
#     plus_pulse,minus_pulse = 1,-1
#     plus_pul_list = [0]
#     minus_pul_list = [0]
#     sum_plus = [ 0 for _ in range(len(sequence)+1)]
#     sum_minus = [ 0 for _ in range(len(sequence)+1)]
    
#     for i in sequence:
#         plus_pul_list.append(i*plus_pulse)
#         minus_pul_list.append(i*minus_pulse)
#         plus_pulse *= -1
#         minus_pulse *= -1
    
#     for i in range(1,len(plus_pul_list)):
#         sum_plus[i] = sum_plus[i-1] + plus_pul_list[i]
    
#     for i in range(1,len(minus_pul_list)):
#         sum_minus[i] = sum_minus[i-1] + minus_pul_list[i]
    
#     max_num = max(map(abs,sum_plus))
#     if max_num in sum_plus:
#         max_idx = sum_plus.index(max_num)
#     else:
#         max_idx = sum_plus.index(-max_num)

#     for i in range(max_idx, 1, -1):
#         if sum_plus[i]

        
    # print(plus_pul_list,minus_pul_list)
    # print(sum_plus,sum_minus)
    
    # return answer

# def solution(sequence):
#     pulse= 1
#     plus_pul_list = [0]
#     sum_plus = [ 0 for _ in range(len(sequence)+1)]
    
#     for i in sequence:
#         plus_pul_list.append(i*pulse)
#         pulse *= -1
    
#     for i in range(1,len(plus_pul_list)):
#         sum_plus[i] = sum_plus[i-1] + plus_pul_list[i]

#     max_num = max(map(abs,sum_plus))
#     if max_num in sum_plus:
#         max_idx = sum_plus.index(max_num)
#     else:
#         sum_plus = list(map(lambda x: -x, sum_plus))
#         plus_pul_list = list(map(lambda x: -x, plus_pul_list))
#         max_idx = sum_plus.index(max_num)

#     for i in range(max_idx, 0, -1):
#         if sum_plus[i] <= 0:
#             if plus_pul_list[i] > 0:
#                 continue
#             else:
#                 return max_num - sum_plus[i]
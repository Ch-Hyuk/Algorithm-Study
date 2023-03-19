from itertools import combinations
23140
# cnt = 0
# for cwr in product([0.1,0.2,0.3,0.4], [0.1,0.2,0.3,0.4],[0.1,0.2,0.3,0.4],[0.1,0.2,0.3,0.4]):
#     print(cwr)
#     cnt += 1
# print(cnt)

# a = [0.1,0.2,0.3,0.4]

# for idx,data in enumerate(a[-1::-1]):
#     print(idx, data)

# cap = 2
# cap_stack = [0 for i in range(cap)]
# print(cap_stack)

# a = [[1, 2, 3], [4, 5, 6]]
# b = [[-1, -2, -3], [1, 1, 1]]
# c = [1, 2, 3]
# d = [5, 6, 7]

# print(zip(a, b))

# print([c - d for c, d in zip(c, d)])

# print(c -1)

# def solution(ingredient):
#     answer = 0
#     if len(ingredient) < 4:
#         return 0
#     for i in range(len(ingredient)):
#         print(i)
#         if ingredient[i] == 1 and ingredient[i+1] == 2 and ingredient[i+2] == 3 and ingredient[i+3] == 1:
#             answer+=1
#             del ingredient[i:i+4]
#             answer += solution(ingredient)
#             break
            
#     return answer

# ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
# print(solution(ingredient))
동규 = 1
print(동규)
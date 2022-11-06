from itertools import permutations, combinations

def solution(nums):
    com = list(combinations(nums, 3))
    res = []
    answer = 0
    for data in com:
        res.append(sum(data)) 
        
    for num in res:
        flag = 0
        if num % 2 == 0:
            continue
        else:
            for i in range(2, num):
                if num % i == 0:
                    flag = 1
            if flag == 0:
                answer+=1
            else:
                continue
    return answer

nums =[1,2,3,4]	
print(solution(nums))
import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2):
        if x < r1:
            max_y = int(math.sqrt(r2**2 - x**2))
            min_y = math.sqrt(r1**2 - x**2)
            answer += int(max_y - min_y)+1
        else:
            answer += int(math.sqrt(r2**2 - x**2))
            
    return (answer + r2 - r1 + 1)*4

print(solution(5, 5))
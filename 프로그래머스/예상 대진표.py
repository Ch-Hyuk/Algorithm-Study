def group(n):
    if n%2 == 0: return n//2
    else: return n//2+1

def solution(n,a,b):
    answer = 1
    while True:
        a, b = group(a), group(b)
        if a == b:
            return answer
        answer += 1
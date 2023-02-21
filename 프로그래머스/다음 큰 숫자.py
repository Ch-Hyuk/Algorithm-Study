def solution(n):
    cnt = bin(n).count('1')
    while True:
        n +=1
        if cnt == bin(n).count('1'):
            return n
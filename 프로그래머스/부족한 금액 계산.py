def solution(price, money, count):
    answer = 0
    res = 0
    for i in range(1,count+1):
        res = res + (price * i)
    answer = res - money

    if answer <= 0:
        answer = 0
    return answer

#등차수열의 합을 이용한 풀이

def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)


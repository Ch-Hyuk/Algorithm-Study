import math
number= ""

def octal_change(n, k):
    global number
    if k == 10:
        for i in str(n):
            number += i
        return
    if n < k:
        number += str(n)
        return
    else:
        number += str(n % k)
        octal_change(n//k, k)
   
def prime_number(n):
    if n == 1:
        return 0
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return 0
    return 1

def solution(n, k):
    answer = 0
    octal_change(n,k)
    re_number = number
    if k != 10:
        re_number = number[::-1]
    num_list = re_number.split("0")
    for data in num_list:
        if data != "":
            answer += prime_number(int(data))

    return answer
    
n = 11011011
k = 10
print(solution(n,k))
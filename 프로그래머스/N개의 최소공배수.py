#3.9 이상에서 math.lcm 작동 가능
import math

def solution(arr):
    lcm_num = 1
    for num in arr:
        lcm_num = int(lcm_num*num/math.gcd(lcm_num,num))
    return lcm_num

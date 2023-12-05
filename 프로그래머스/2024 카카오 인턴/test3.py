from itertools import combinations, product
from collections import Counter

def dice_sum(dice_list):
    sum_list = []
    for pro in product(*dice_list):
        sum_list.append(sum(pro))

    return sum_list

def wining_case(a_dice, b_dice):
    cnt = 0
    A_cnt = Counter(a_dice)
    B_cnt = Counter(b_dice)

    for a_key, a_value in A_cnt.items():
        for b_key, b_value in B_cnt.items():
            if a_key > b_key:
                cnt += a_value * b_value

    return cnt

def solution(dice):
    A_dice,B_dice,answer = [],[],[]
    max_per = [-1,[]]
    A_dice = list(combinations(dice, len(dice)//2))

    for com in A_dice:
        b_list = []
        for item in dice:
            if item not in com:
                b_list.append(item)
        B_dice.append(b_list)

    for i in range(len(A_dice)):
        result_dice = A_dice[i]
        a, b = dice_sum(A_dice[i]),dice_sum(B_dice[i])
        wining_value = wining_case(a, b)

        if wining_value > max_per[0]:
            max_per[0] = wining_value
            max_per[1] = result_dice

    for i, data in enumerate(dice):
        for num in max_per[1]:
            if num == data:
                answer.append(i+1)
    
    return answer
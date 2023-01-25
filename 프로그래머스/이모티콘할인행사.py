from itertools import product

def solution(users, emoticons):
    result = [0,0]
    percent = [10,20,30,40]
    for cwr in product(percent, repeat=len(emoticons)):
        emoticons_plus = 0
        total_cost = 0

        for user in users:
            user_cost = 0
            for i in range(len(emoticons)):
                if user[0] <= cwr[i]:
                    user_cost += emoticons[i]*(100-cwr[i])//100

            if user[1] <= user_cost:
                emoticons_plus += 1

            else:
                total_cost += user_cost

        if result[0] < emoticons_plus:
            result[0] = emoticons_plus
            result[1] = total_cost

        elif result[0] == emoticons_plus:
            result[1] = max(result[1],total_cost)

    return result
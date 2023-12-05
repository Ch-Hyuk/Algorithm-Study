from collections import defaultdict

def solution(friends, gifts):
    dic_name = {}
    gift_jisoo = {}
    answer = [0 for _ in range(len(friends))]

    for idx,name in enumerate(friends):
        dic_name[name] = idx
        gift_jisoo[idx] = 0

    gift_list = [[0 for _ in range(len(friends))] for _ in range(len(friends))]

    for gift in gifts:
        print(gift)
        send, take = gift.split()
        send = dic_name[send]
        take = dic_name[take]

        gift_list[send][take] += 1

        gift_jisoo[send] += 1
        gift_jisoo[take] -= 1
        
    for i in range(1, len(friends)):
        for j in range(0 , i):
            if gift_list[i][j] > gift_list[j][i]:
                answer[i] += 1
            elif gift_list[i][j] < gift_list[j][i]:
                answer[j] += 1
            
            else:
                if gift_jisoo[i] > gift_jisoo[j]:
                    answer[i] += 1
                elif gift_jisoo[i] < gift_jisoo[j]:
                    answer[j] += 1
    return max(answer)   
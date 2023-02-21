from collections import Counter

def solution(topping):
    answer = 0
    me_dic = Counter(topping)
    bro_dic = {}
    for i in topping:
        if i not in bro_dic:
            bro_dic[i] = 1
        else:
            bro_dic[i] +=1 
        me_dic[i] -= 1
        if me_dic[i] <= 0:
            del me_dic[i]

        if len(me_dic.keys()) == len(bro_dic.keys()):
            answer+= 1
            
    return answer
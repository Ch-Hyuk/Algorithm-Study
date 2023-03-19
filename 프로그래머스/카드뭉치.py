def solution(cards1, cards2, goal):
    c1,c2 = 0,0
    word_dic = {}
    for i, data in enumerate(cards1):
        word_dic[data] = (1,i)

    for i, data in enumerate(cards2):
        word_dic[data] = (2,i)

    for data in goal:
        if word_dic[data][0] == 1 and word_dic[data][1] == c1:
            c1 += 1
            continue

        if word_dic[data][0] == 2 and word_dic[data][1] == c2:
            c2 += 1
            continue

        return "No"
    return "Yes" 
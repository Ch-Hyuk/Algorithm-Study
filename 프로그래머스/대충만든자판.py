def solution(keymap, targets):
    answer = []
    key_dic = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in key_dic.keys():
                key_dic[key[i]] = i+1

            elif key_dic[key[i]] > i+1:
                key_dic[key[i]] = i+1

    for key in targets:
        cnt = 0
        for data in key:
            if data not in key_dic.keys():
                cnt = -1
                break

            cnt += key_dic[data]
        answer.append(cnt)
    return answer

    
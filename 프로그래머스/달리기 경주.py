def solution(players, callings):
    answer = []
    rank_dic = {idx:data for idx, data in enumerate(players)}
    name_dic = {data:idx for idx, data in enumerate(players)}

    for overtaker in callings:
        past_rank = name_dic[overtaker]
        present_rank = name_dic[overtaker] - 1
        caught_player = rank_dic[present_rank]

        rank_dic[present_rank] = overtaker
        rank_dic[past_rank] = caught_player
        name_dic[caught_player] += 1
        name_dic[overtaker] -= 1

    return [name for idx, name in rank_dic.items()]
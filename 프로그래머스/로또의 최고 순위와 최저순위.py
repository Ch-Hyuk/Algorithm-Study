def solution(lottos, win_nums):
    cnt_min = len(set.intersection(set(lottos),set(win_nums)))
    cnt_max = cnt_min + lottos.count(0)    
    if cnt_max == 0:
        min_rank = 6
    else:
        min_rank = 7-cnt_max
    if cnt_min == 0:
        max_rank = 6
    else:
        max_rank = 7-cnt_min
    answer = [min_rank, max_rank]
    return answer

#미친놈

def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

#미친놈 2
def solution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]

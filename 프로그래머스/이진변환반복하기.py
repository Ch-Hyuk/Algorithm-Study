def solution(s):
    answer = list(bin_recur(s))
    return answer

def bin_recur(s):
    if s == '1':
        zero_cnt =0
        rec_cnt = 0
        return rec_cnt , zero_cnt
    pre_zero_cnt = s.count('0')
    pre_recur_cnt = 1
    rec_cnt, zero_cnt = bin_recur(bin(len(s.replace('0',''))).replace('0b',''))
    return  rec_cnt+pre_recur_cnt, zero_cnt+pre_zero_cnt

s = "110010101001"
solution(s)
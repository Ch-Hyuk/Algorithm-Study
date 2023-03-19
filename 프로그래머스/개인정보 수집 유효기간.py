def solution(today, terms, privacies):
    answer = []
    term_dic = {}
    t_y,t_m,t_d = map(int,today.split('.'))
    for i in terms:
        term_dic[i[0]] = int(i[1:])
        
    for i,data in enumerate(privacies):
        y,m,d = map(int,data[:-2].split('.'))
        m += term_dic[data[-1]]
        if m > 12 and m%12 != 0:
            m,y = m%12, y+m//12
        if m > 12 and m%12 == 0:
            m,y = 1, y-1+m//12
        print(t_y,t_m,t_d)
        print(y,m,d)
        if t_y > y:
            answer.append(i+1)
        if t_y == y and t_m > m:
            answer.append(i+1)
        if t_y == y and t_m == m and t_d >= d:
            answer.append(i+1)
            
    return answer

print(solution("2021.12.08", ["A 18"], ["2020.06.08 A"]))
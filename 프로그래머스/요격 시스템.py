def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x:(x[0],-x[-1]))
    s, e = -1, -1
    
    for x,y in targets:
        if x < e:
            if y < e:
                s,e = x,y
        else:
            answer += 1
            s,e = x,y
            
    return answer
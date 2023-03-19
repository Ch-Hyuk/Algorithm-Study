def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) -s
    for i in sorted(r):
        if i-1 in l:
            l.remove(i-1)
            
        elif i+1 in l:
            l.remove(i+1)
    return n - len(l)

n= 5
lost = [2,4]
reserve = [1,3,5]
print(solution(n, lost, reserve))

def solution(n, lost, reserve):
    u = [1] * (n+2)
    for i in reserve:
        u[i] += 1
    for i in lost:
        u[i] -= 1
    for i in range(1, n + 1):
        if u[i-1] == 0 and u[i] == 2: 
            u[i-1],u[i] = 1, 1      #u[i -1:i + 1] = [1, 1]
        elif u[i] == 2 and u[i+1] == 0:
            u[i], u[i+2] == 1, 1
    
    #return len([x for x in u[1:-1] if x > 0 ])
    return n - u.count(0)

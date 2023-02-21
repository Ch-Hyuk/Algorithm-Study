def solution(s, skip, index):
    answer = ''
    skip_list = []
    for i in skip:
        skip_list.append(ord(i))
        skip_list.append(ord(i)+26)
        skip_list.append(ord(i)+52)
    
    for st in s:
        cnt = 0
        visited = []
        while 1:
            if len(visited) == len(range(ord(st)+1,ord(st)+index+cnt+1)):
                break
            for i in range(ord(st)+1,ord(st)+index+1+cnt):
                if i in visited:
                    continue
                    
                if i in skip_list:
                    cnt += 1
                    visited.append(i)
                else:
                    visited.append(i)
                
        if ord(st)+index+cnt >=123 and ord(st)+index+cnt < 149 :
            answer += chr((ord(st)+index+cnt)-26)
        elif ord(st)+index+cnt >=149:
            answer += chr((ord(st)+index+cnt)-52)
        else:
            answer += chr(ord(st) + index + cnt)
    return answer

s = "z"
skip = 'abcdefghij'
index = 20
print(solution(s, skip, index))

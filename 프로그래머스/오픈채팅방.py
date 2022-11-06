def solution(record):    
    answer = []
    dic ={}
    for data in record:
        re_data = data.split()
        if re_data[0] == 'Enter' or re_data[0] == 'Change':
            dic[re_data[1]] = re_data[2]
    
    for data in record:
        re_data = data.split()
        if re_data[0] == 'Enter':
            e_str = dic[re_data[1]] + "님이 들어왔습니다."
            answer.append(e_str)

        if re_data[0] == 'Leave':
            answer.append(dic[re_data[1]] + "님이 나갔습니다.")
        
    print(answer)
    return answer

record =["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)

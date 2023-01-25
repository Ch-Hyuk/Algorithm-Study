def solution(storey):
    answer = 0
    num_str = str(storey)[::-1]
    flag = 0
    for idx,num in enumerate(num_str):
        number = int(num)
        if number > 5:
            answer += 10-number -flag
            flag = 1

            if idx == len(num_str) -1:
                answer += 1

        elif number == 5:
            if idx == len(num_str) -1:
                return answer + 5

            if flag == 1:
                answer += 4
                flag = 1
            
            elif int(num_str[idx+1]) >= 5 :
                answer += 5
                flag = 1
            
            else:
                answer += 5
                flag = 0
                
        else:
            answer += number + flag
            flag = 0
            
    return answer
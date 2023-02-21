def solution(book_time):
    room_dic = {}
    time_list = []
    for data in book_time:
        start_time = int(data[0].replace(':',''))
        if int(data[1].replace(':','')[2:]) >= 50:
            end_time = int(data[1].replace(':',''))+50
        else:
            end_time = int(data[1].replace(':',''))+10
        time_list.append((start_time,end_time))

    time_list.sort(key=lambda x: x[0])
    room_dic[0] = time_list[0]

    for time in time_list[1:]:
        flag = False
        for key in range(len(room_dic)):
            if room_dic[key][1] <= time[0]:
                room_dic[key] = time
                flag = True
                break

        if flag is False:
            room_dic[len(room_dic)] = time

    return len(room_dic)

book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]

print(solution(book_time))
def solution(plans):
    answer = []
    curr_time = "00:00" # 시작 시간
    paused = [] # 멈춰둔 과제들을 담는 리스트

    for i in range(len(plans)):
        name, start, playtime = plans[i]
        start_time = start.split(":") # 시작 시간을 시와 분으로 분리
        end_time = [str((int(start_time[0]) + (int(start_time[1]) + int(playtime)) // 60) % 24).zfill(2), str((int(start_time[1]) + int(playtime)) % 60).zfill(2)] # 끝나는 시간을 계산
        
        while paused and curr_time >= paused[-1][1]: # 멈춰둔 과제들 중에서 끝낸 과제가 있는지 확인
            answer.append(paused.pop()[0]) # 끝낸 과제 이름을 정답에 추가
        
        if curr_time < start: # 새로운 과제 시작
            curr_time = start
        else: # 진행 중인 과제를 멈추고 새로운 과제 시작
            paused.append((name, end_time))
            paused.sort(key=lambda x: x[1], reverse=True) # 멈춰둔 과제들을 최근에 멈춘 과제부터 처리하기 위해 정렬
            name, end_time = paused.pop()
            curr_time = end_time

        answer.append(name) # 과제 이름을 정답에 추가
    
    while paused: # 마지막으로 멈춰둔 과제들 처리
        answer.append(paused.pop()[0])

    return answer
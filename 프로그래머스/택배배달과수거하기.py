n = 5
c = 4
delivers = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]
re_delivers = delivers[::-1]
re_pickups = pickups[::-1]
answer = 0
while(1):
    cap= [c, c]
    result = 0
    start = 0
    if re_delivers[idx] == 0 and re_pickups[idx] == 0 or cap[0] == 0 and cap[1] == 0:
        start += 1
   
    for idx in range(start,n):
        if re_delivers[idx] == 0 and re_pickups[idx] == 0 or cap[0] == 0 and cap[1] == 0:
            continue

        if result == 0 and (re_delivers[idx] != 0 or re_pickups[idx] != 0):
            result = (n-idx)*2

        if re_delivers[idx] >= cap[0]:
            re_delivers[idx] -= cap[0]
            cap[0] = 0

        else:
            cap[0] -= re_delivers[idx]
            re_delivers[idx] = 0
 
        if re_pickups[idx] >= cap[1]:
            re_pickups[idx] -= cap[1]
            cap[1] = 0
        else:
            cap[1] -= re_pickups[idx]
            re_pickups[idx] = 0

        print(re_delivers,re_pickups)

    if result == 0:
        print(answer)
        break
    else:
        print("result: ",result)
        answer += result

    

        


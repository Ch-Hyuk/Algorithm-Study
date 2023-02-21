def solution(cap, n, deliveries, pickups):
    re_deliveries = deliveries[::-1]
    re_pickups = pickups[::-1]
    answer = 0
    start = 0
    while start != n:
        cap_li= [cap, cap]
        result = 0
        for i in range(start, n):
            if re_deliveries[i] == 0 and re_pickups[i] == 0:
                start += 1
                continue

            if re_deliveries[i] != 0 or re_pickups[i] != 0:
                result = (n-i)*2
                break

        if result == 0:
            return answer
        else:
            answer += result
    
        for idx in range(start, n):
            if cap_li[0] == 0 and cap_li[1] == 0 or cap_li[1] == 0 and re_deliveries[idx] == 0 or cap_li[0] == 0 and re_pickups[idx] == 0:
                continue

            if re_deliveries[idx] >= cap_li[0]:
                re_deliveries[idx] -= cap_li[0]
                cap_li[0] = 0

            else:
                cap_li[0] -= re_deliveries[idx]
                re_deliveries[idx] = 0
 
            if re_pickups[idx] >= cap_li[1]:
                re_pickups[idx] -= cap_li[1]
                cap_li[1] = 0
            else:
                cap_li[1] -= re_pickups[idx]
                re_pickups[idx] = 0
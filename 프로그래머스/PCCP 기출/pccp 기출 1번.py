def solution(bandage, health, attacks):
    present_health = [health for _ in range(attacks[-1][0]+1)]
    start_time = attacks[0][0]
    attacks_idx = 0
    time, bandage_time = start_time, 1
    
    while time < len(present_health):
        recover = 0
        
        if attacks[attacks_idx][0] == time:
            damage = attacks[attacks_idx][1]
            if damage >= present_health[time-1]:
                return -1
            
            else:
                present_health[time] = present_health[time-1] - damage
                time += 1
                attacks_idx += 1
                continue
                
        if present_health[time-1] < health:
            recover += bandage[1]
            
            if bandage_time == bandage[0]:
                recover += bandage[2]
                bandage_time = 0
            
            bandage_time += 1
        
        result = present_health[time-1] + recover
        
        if result >= health:
            present_health[time] = health
        else:
            present_health[time] = result
            
        time += 1
    
    print(present_health)
    return present_health[-1]

print(solution([3, 2, 7],20,[[1, 15], [5, 16], [8, 6]]))
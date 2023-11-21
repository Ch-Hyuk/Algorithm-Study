from datetime import datetime as dt
import math

def solution(fees, records):
    basic_time, basic_rate, unit_time, unit_fee = fees
    car_dict = {}
    acc_time = {}
    answer = []
    
    for record in records:
        time, car_num, fl = record.split(' ')
    
        if fl == 'OUT':
            hours, mine, _  = map(int, str(dt.strptime(time,'%H:%M') - dt.strptime(car_dict[car_num],'%H:%M')).split(':'))
            acc_time[car_num] += (hours*60 + mine)
            del car_dict[car_num]
            
        if fl == 'IN':
            if car_num not in acc_time.keys():
                acc_time[car_num] = 0
            
            car_dict[car_num] = time
    
    for car_num, entry_time in car_dict.items():
        hours, mine, _  = map(int, str(dt.strptime("23:59",'%H:%M') - dt.strptime(entry_time,'%H:%M')).split(':'))
        acc_time[car_num] += (hours*60 + mine)
    
    for car_num in sorted(acc_time):
        if basic_time < acc_time[car_num]:
            answer.append(basic_rate + math.ceil((acc_time[car_num]-basic_time)/unit_time)*unit_fee)
        
        else:
            answer.append(basic_rate)

    return answer
import sys

gear_state ={}
answer = 0

def gear_rotation(gear_num, rotation):
    if rotation == 1:
        change_pole = gear_state[gear_num][-1]
        stay_pole = gear_state[gear_num][:-1]
        gear_state[gear_num] = change_pole + stay_pole
    
    elif rotation == -1:
        change_pole = gear_state[gear_num][0]
        stay_pole = gear_state[gear_num][1:]
        gear_state[gear_num] = stay_pole + change_pole

def check_l(gear_num, rotation):
    if gear_num < 1:
        return
    elif gear_num == 1:
        gear_rotation(gear_num, rotation)
        return

    if gear_state[gear_num][6] != gear_state[gear_num-1][2]:
        check_l(gear_num-1, rotation*-1)
        gear_rotation(gear_num, rotation)
    else:
        gear_rotation(gear_num, rotation)

def check_r(gear_num, rotation):
    if gear_num > 4:
        return
    elif gear_num == 4:
        gear_rotation(gear_num, rotation)
        return

    if gear_state[gear_num][2] != gear_state[gear_num+1][6]:
        check_r(gear_num+1, rotation*-1)
        gear_rotation(gear_num, rotation)
    else:
        gear_rotation(gear_num, rotation)

def total_score():
    global answer
    for gear_num in range(1, 5):
        if gear_state[gear_num][0] == '1':
            answer = answer + (2 ** (gear_num-1))

    return answer

if __name__ == '__main__':
    for gear_num in range(1, 5):
        gear = input()
        gear_state[gear_num] = gear

    rotation_num = int(input())


    for k in range(rotation_num):
        gear_num, rotation = map(int,sys.stdin.readline().split())

        check_l(gear_num, rotation)
        gear_rotation(gear_num, rotation*-1)
        check_r(gear_num,rotation)

    print(total_score())
def search(bin_num):
    center_idx = len(bin_num)//2
    print(bin_num, center_idx)

    if bin_num[center_idx] == '0' and bin_num[center_idx+1] == '1' or bin_num[center_idx] == '0' and bin_num[center_idx-1] == '1':
        #print("조건 안맞음")
        return 0
    
    if len(bin_num[:center_idx]) >= 3:
        left_node = search(bin_num[:center_idx])
        if left_node == 0: return 0

    if len(bin_num[center_idx+1:]) >= 3:
        right_node = search(bin_num[center_idx+1:])
        if right_node == 0: return 0

    return 1

def solution(numbers):
    answer = []
    for i in numbers:
        n = 0
        bin_num = bin_num = bin(i)[2:]
        while True:
            if 2**n <= len(bin_num) and len(bin_num) < 2**(n+1):
                #print("숫자: ",bin_num)
                a = search(bin_num.zfill(2**(n+1)-1))
                #print(a)
                answer.append(a)
                break
            n += 1
    return answer


numbers= []
for i in range(1, 100):
    numbers.append(i)
numbers = [1152,1,10**11]
print(solution(numbers))
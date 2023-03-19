def solution(number, k):
    num = []
    for i in number:
        num.append(i)
        while k > 0 and len(num) > 1 and num[-2] < num[-1]:
            num.pop(-2)
            k -= 1
    
    return ''.join(num[:-k]) if k > 0 else ''.join(num)

number = '1924'
k = 2
print(solution(number,k))
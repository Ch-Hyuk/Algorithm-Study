def solution(N, number):
    s = [set() for x in range(8)]
    for i, data in enumerate(s, start=1):
        data.add(int(str(N) * i))  
    for i in range(len(s)):
        for j in range(i):
            for num1 in s[j]:
                for num2 in s[i - j - 1]:
                    s[i].add(num1 - num2)
                    s[i].add(num1 + num2)
                    s[i].add(num1 * num2)
                    if num2 != 0:
                        s[i].add(num1 // num2)
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1
    return answer
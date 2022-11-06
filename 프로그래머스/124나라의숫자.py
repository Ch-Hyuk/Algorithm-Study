def rec(num):
    if num // 3 == 0:
        if num == 1 or num ==2:
            return num
        elif num == 3:
            return 4

    elif num % 3 == 1:
        return int(str(rec(num//3))+"1")

    elif num % 3 == 2:
        return int(str(rec(num//3))+"2")

    elif num % 3 == 0:
        if num // 3 == 1:
            return 4
        else:
            return int(str(rec(num//3-1))+"4")

print(rec(3))
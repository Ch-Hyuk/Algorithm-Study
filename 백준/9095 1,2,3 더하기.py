T = int(input())
num =[1,1,2,4]

def rec(n):
    if n <= 3:
        return num[n]
    
    return rec(n-1)+rec(n-2)+rec(n-3)

for _ in range(T):
    print(rec(int(input())))
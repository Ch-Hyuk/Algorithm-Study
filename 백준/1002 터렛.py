import sys

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,sys.stdin.readline().split())

    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5

    if distance > r1+r2:
        print(0)

    elif distance == r1+r2:
        print(1)

    elif distance < r1+r2:
        if x1 == x2 and y1 == y2 and r1 == r2:
            print(-1)
        elif x1 == x2 and y1 == y2 and r1 != r2:
            print(0)
        
        elif abs(r2 - r1) > distance:
            print(0)

        elif abs(r2 - r1) == distance:
            print(1)

        else:
            print(2) 


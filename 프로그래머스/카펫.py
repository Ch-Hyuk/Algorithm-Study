def solution(brown, yellow):
    x_plus_y,x_multi_y = (brown+4)//2, brown+yellow
    for i in range(3,int(x_multi_y**1/2)+1):
        if x_multi_y % i == 0 and x_multi_y // i + i == x_plus_y:
            return [x_multi_y // i, i]
        

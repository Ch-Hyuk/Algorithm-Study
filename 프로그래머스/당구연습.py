import math

def solution(m, n, startX, startY, balls):
    answer = []
    for i in balls:
        distance_list = []
        if startX == i[0]:
            if startY > i[1]:
                xy_list = [(i[0],2*n - i[1]),(2*m - i[0], i[1]),(-i[0],i[1])]
            else:
                xy_list = [(i[0],-i[1]),(2*m - i[0], i[1]),(-i[0],i[1])]
        elif startY == i[1]:
            if startX > i[0]: 
                xy_list = [(i[0],2*n - i[1]),(i[0],-i[1]),(2*m - i[0], i[1])]
            else:
                xy_list = [(i[0],2*n - i[1]),(i[0],-i[1]),(-i[0],i[1])]
        else:
            xy_list = [(i[0],2*n - i[1]),(i[0],-i[1]),(2*m - i[0], i[1]),(-i[0],i[1])]

        for j in xy_list:
            distance_list.append(round((math.dist(j,(startX,startY)))**2))
        answer.append(min(distance_list))
    return answer
def solution(park, routes):
    dir_dic = {'S':[1,0],'N':[-1,0],'E':[0,1],'W':[0,-1]}
    location = list()
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                location = [i,j]
    
    for i in routes:
        start = location
        dir,cnt = i[0],int(i[-1])
        while cnt > 0:
            row, col = start
            dr = row + dir_dic[dir][0]
            dc = col + dir_dic[dir][1]

            if  dr < 0 or dc < 0 or dr >= len(park) or dc >= len(park[0]) or park[dr][dc] == 'X':
                break

            start = [dr, dc]
            print(location)
            cnt -= 1

        if cnt == 0: location = start
    return location

park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]
print(solution(park, routes))
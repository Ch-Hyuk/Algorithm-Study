def solution(tickets):
    route_dic = {}
    for i in tickets:
        route_dic[i[0]] = route_dic.get(i[0], []) + [i[1]]
    
    for i in route_dic:
        route_dic[i].sort(reverse = True)
    
    stack = ['ICN']
    path = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in route_dic or len(route_dic[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(route_dic[top][-1])
            route_dic[top].pop()
    return path[::-1]
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = []
    

class LinkedList:
    def __init__(self, data):
        self.head = None
        self.build_time = data

    def dfs(self, data):
        current = data
        if len(current.next) == 0:
            return 0
        
        time_list = []
        for d in current.next:
            time = 0
            time = max(time, self.dfs(d))
            time += self.build_time[d.data]
            time_list.append(time)
        return max(time_list)

input = sys.stdin.readline  

T = int(input()) 

for _ in range(T):

    nodes = {}
    N, K = map(int, input().split())

    for i in range(N):
        node = Node(i)
        nodes[i] = node


    build_time = list(map(int, input().split()))
    build = LinkedList(build_time)
    for order in range(K):
        x, y = map(int, input().split())
        node_a = nodes[x-1]
        node_b = nodes[y-1]
        node_b.next.append(node_a)
    
    W = int(input())-1
    build.head = nodes[W]
    print(build.dfs(nodes[W])+build_time[nodes[W].data])
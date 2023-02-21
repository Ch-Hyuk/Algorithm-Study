class Node:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None
        # print("node생성")

class BST:
    def __init__(self):
        self.root = None
        self.sheep_cnt = 0
        self.wolf_cnt = 0
    
    def dfs(self, n):
        if n.node == 1:
            self.wolf_cnt += 1
        else:
            self.sheep_cnt += 1

        if self.sheep_cnt - self.wolf_cnt <= 0:
            self.wolf_cnt -= 1
            print("잡아먹음return")
            return

        if n != None:
            while 1:
                print("현재 노드{}, 양의 개수{}, 늑대 개수{}".format(n.node, self.sheep_cnt, self.wolf_cnt))

                if n.left != None:
                    print("왼쪽 노드")
                    self.dfs(n.left)
                if n.right != None:
                    print("오른쪽 노드")
                    self.dfs(n.right)
                if n.node == 1:
                    self.wolf_cnt -= 1
                    return
                else:
                    return


def solution(info, edges): 
    answer = 0 
    node_dic = {}
    tree = BST()
    for idx, data in enumerate(info):
        node_dic[idx] = Node(data)
    
    tree.root = node_dic[0]
    for node, c_node in edges:

        if node_dic[node].left == None:
            node_dic[node].left = node_dic[c_node]
        else:
            node_dic[node].right = node_dic[c_node]

    print(node_dic)
    tree.dfs(tree.root)
    return tree.sheep_cnt


info = [0,0,1,1,1,0,1,0,1,0,1,1]
# info = [0,1,2,3,4,5,6,7,8,9,10,11]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info, edges))
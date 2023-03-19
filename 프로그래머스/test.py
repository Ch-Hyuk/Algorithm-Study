# # import math

# # def solution(k, d):
# #     cen_point = d/2*math.sqrt(2)
# #     answer = (int(cen_point)//k+1)**2+2
# #     for i in range(0, d, k):

# #         if i <= cen_point:
# #             print(i)
# #             continue
# #         for j in range(0, int(cen_point)+1, k):
# #             if math.sqrt(i**2+j**2) <= d:
# #                 answer += 2
    
# #     return answer
동규 = 1

# def solution(cards):
#     group = []
#     visited = set()
#     for i in range(1,len(cards)+1): 
#         cnt = 0
#         if cards[i-1] in visited:
#             continue
        
#         box = cards[i-1]
#         while box not in visited:
#             visited.add(box)
#             cnt+=1
#             box = cards[box-1]
            
#         group.append(cnt)
        
#     group.sort(reverse = True)    
    
#     return group[0] * group[1]

# cards = [2,1]
# print(solution(cards))

# from collections import defaultdict

# def solution(alp, cop, problems):
#     answer = 0
#     pos_problems = set()   #풀수 있는 문제 idx
#     # best_problems = [0,0]  #풀수 있는 문제중 alp 최대, cop 최대
#     dic_problems = defaultdict(list)
#     problems.sort(key=lambda x: (x[0],x[1]))
    
#     min_alp, min_cop = 200 ,200
#     max_alp,max_cop = -1, -1
#     for i in problems:
#         print(i)
#         dic_problems[i[4]].append(i)
#         print(dic_problems)
#         if i[0] <= alp and i[1] <= cop:
#             pos_problems.add(i)
        
#         if min_alp > i[0]:min_alp = i[0]
#         if min_alp > i[1]:min_alp = i[1]
#         if max_alp < i[0]:max_alp = i[0]           
#         if max_cop < i[1]:max_cop = i[1]
        
#     while True:
#         if alp >= max_alp and cop >= max_cop:
#             return answer
    
#         if alp < min_alp and cop < min_cop:
#             answer += (min_alp+min_cop)
#             pos_problems.add()
#             alp = min_alp
#             cop = min_cop

# today = "2022.05.19"
# y,m,d = map(int,today.split('.'))
# print(y)

# "2020.01.02", ["A", 1], ["2020.01.02 A"], []
# "2021.12.08", ["A 18"], ["2020.06.08 A"], [1]


# def solution(L, x):
#     left,right= 0,len(L)-1
    
#     while left <= right:
#         middle = (right+left)//2
#         print(middle)
#         if middle == 0: return -1
#         if L[left] == x:return left
#         if L[right] == x:return right
#         if L[middle] == x:return middle
        
#         if L[middle] < x:right = middle
            
#         if L[middle] > x:left = middle
        
#     return -1

# solution([2, 5, 7, 9, 11], 4)


class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def __repr__(self):
        if self.nodeCount == 0:
            return 'empty'

        s= ''
        curr = self.head
        while curr is not None:
            s+= repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s
    
    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        
        curr = self.getAt(pos)

        if self.nodeCount == 1:
            self.nodeCount -= 1
            self.head = None
            self.tail = None
            return curr.data
        
        if pos == 1:
            self.head = curr.next
        
        else:
            prev = self.getAt(pos-1)
            if curr == self.tail:
                self.tail = prev
                prev.next = None
            else:
                prev.next = curr.next
                
                
        self.nodeCount -= 1
        return curr.data


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

    
a = LinkedList()

a= Node(1)
b= Node(2)
c= Node(3)
d= Node(4)
e= Node(5)
f= Node(6)

L = LinkedList()
L.traverse()
L.insertAt(1, a)
# L.insertAt(2, b)
# L.insertAt(3, c)
# L.insertAt(4, d)
# L.insertAt(5, e)
print(L.traverse())
print(L.popAt(1))
print(L.traverse())


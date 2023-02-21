
####순열과 조합####
from itertools import chain
li = [1, 2, 3]
li2 = [4,5,6]
from itertools import permutations #순열 permutations(iterable, r = None) None이면 최대길이 순열

print(list(map(''.join,permutations(li, 2))))   # 2개의 원소로 순열 list 만들기
print(list(chain(permutations(li))))            #list만드는 여러 방법, chain 사용

pe_li = []
for i in permutations(li):
    pe_li.append(i)
print(pe_li)                       #[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

from itertools import product #중복 순열 product(*iterable, repeat = number) 여러 iterate 간의 모든 순열, 같은 iterate라면 repeat 수만큼 반복
po_li = []
for i in product(li,li2, repeat=1):
    po_li.append(i)
print(po_li)                       #[(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

from itertools import combinations #조합 combinations(iterable, r) iter 중 r개 조합 
co_li = []
for i in combinations(li, 2):
    co_li.append(i)
print(co_li)                       #[(1, 2), (1, 3), (2, 3)]

from itertools import combinations_with_replacement # 중복 조합 combinations_with_replacement(iterable, r) iter 중 r개인 중복 조합
combi_li = []
for i in combinations_with_replacement(li, 3):
    combi_li.append(i)
print(combi_li)                    #[(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 2), (1, 2, 3), (1, 3, 3), (2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, 3)]




####정렬#### 
#sort(): 리스트 매서드, 기존 리스트를 변화
#sorted(): 파이썬 내장함수, 새로운 정렬 결과를 반환

a = [2,4,7,23,78,1,7]
b = [1,6,2,4,5,8,3]
a.sort()
print(a)                        #[1, 2, 4, 7, 7, 23, 78]
a.sort(reverse=True) # 내림차순

b_sort = sorted(b)
b_re_sort = sorted(b, reverse = True) #내림차순
print(b)                        #[1, 6, 2, 4, 5, 8, 3] 기존 list 변화 x
print(b_sort)                   #[1, 2, 3, 4, 5, 6, 8]

#key option 활용
#정렬을 목적으로 하는 함수를 값으로 넣는다. lambda를 자주 이용함 sort(), sorted() 모두 가능

str_li = ['ac', 'abasd', 'ce', 'baefe', 'fagag', 'e']
tu_li = [(1,1), (0,5), (5,2), (2,2), (0,3), (3,7)]
a_li = sorted(str_li, key=len)
print(a_li)                     #['e', 'ac', 'ce', 'abasd', 'baefe', 'fagag']

b_li = sorted(str_li, key=lambda x:x[0]) #각 인스턴스의 첫 번째 문자열에 따라 정렬
print(b_li)                     #['ac', 'abasd', 'baefe', 'ce', 'e', 'fagag']

c_li = sorted(tu_li, key=lambda x:(x[0],-x[1])) #첫 번째 index기준으로 정렬 같다면 두 번째 index 기준으로 내림차순 정렬
print(c_li)



####collections 모듈####
##Counter: 각 원소가 몇번씩 나오는지 저장된 객체를 얻음 dict 형태
from collections import Counter
Counter_li = [1,1,1,2,2,2,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,6,6,7,8]
counter = Counter(Counter_li)
print(counter)  #Counter({5: 7, 4: 6, 1: 3, 2: 3, 3: 2, 6: 2, 7: 1, 8: 1})

#most_common() 데이터가 많은 순으로 튜플로 정렬
print(counter.most_common())    #[(5, 7), (4, 6), (1, 3), (2, 3), (3, 2), (6, 2), (7, 1), (8, 1)]



##defaultdict: 딕셔너리에서 키가 없는 상황에서 필요에 의해 사용 키가 없어도 default로 값이 들어가 있음
from collections import defaultdict
de_dict = defaultdict(int) #int == lambda:0 -> 0을 반환, list, tuple .. 등이 들어가도 됨
de_dic = defaultdict(list)
print(de_dic[0])
for i in range(10):
    de_dict[i] += 1        #key가 존재하지 않아도 에러가 발생하지 않음
print(de_dict)                  #defaultdict(<class 'int'>, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1})

#deque: 양방향 큐
from collections import deque
que_li = [1,2,3,4,5,6,7,8]
sample_li = ['zz','zwef','adf']
que = deque(que_li)
print(que)                      #deque([1, 2, 3, 4, 5, 6, 7, 8])

que.append('a')
print(que)                      #deque([1, 2, 3, 4, 5, 6, 7, 8, 'a'])
que.appendleft('b')
print(que)                      #deque(['b', 1, 2, 3, 4, 5, 6, 7, 8, 'a'])

print(que)                      #deque(['b', 1, 2, 3, 4, 5, 6, 7, 8, 'a', 'zz', 'zwef', 'adf'])
que.extendleft(sample_li)
print(que)                      #deque(['adf', 'zwef', 'zz', 'b', 1, 2, 3, 4, 5, 6, 7, 8, 'a', 'zz', 'zwef', 'adf'])

p = que.pop()                   #pop하여 변수 할당 가능
print(que)                      #deque(['adf', 'zwef', 'zz', 'b', 1, 2, 3, 4, 5, 6, 7, 8, 'a', 'zz', 'zwef'])
print(p)                        #adf
que.popleft()
print(que)                      #deque(['zwef', 'zz', 'b', 1, 2, 3, 4, 5, 6, 7, 8, 'a', 'zz', 'zwef'])

que.reverse()
print(que)                      #deque([8, 7, 6, 5, 4, 3, 2, 1, 'b', 'zz', 'zwef'])
que.rotate()                    #마지막 index 첫 index로 옮김
print(que)                      #deque(['zwef', 8, 7, 6, 5, 4, 3, 2, 1, 'b', 'zz'])

que.remove(1)
print(que)                      #deque(['zwef', 'zz', 'b', 2, 3, 4, 5, 6, 7, 8])
que.clear()
print(que)                      #deque([])
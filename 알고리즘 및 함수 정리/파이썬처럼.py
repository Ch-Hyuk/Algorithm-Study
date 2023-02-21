#몫, 나머지 divmod(), *을 이용한 unpacking
a, b = 5, 7
print(*divmod(a, b))    



#문자열 정렬
s = "abcd"
n = 7

print(s.ljust(n))       #abcd   
print(s.center(n))      #    abcd
print(s.rjust(n))       #       abcd



#알파벳, 숫자 
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789



#zip의 사용: 여러 리스트에서 값을 동시에 뽑아낼 수 있다. 여러개 동시에 순회할 때도 사용
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

newlist = list(map(list, zip(*mylist)))

print(newlist)



#zip 응용
def solution(mylist):
    answer = []
    for i in range(len(mylist)-1):
        answer.append(abs(mylist[i] - mylist[i+1]))
    return answer

#index에 접근하지 않고 각 원소에 접근, 동일한 리스트를 여러개 가능, 길이가 다를 때는 짧은 쪽 까지만 이터레이션이 이루어짐
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer



#map의 사용
#ex) 리스트의 type 변환
list1 = ['1', '100', '33']
list2 = []
for value in list1:
    list2.append(int(value))

#for문을 사용하지 않고 변경 가능
list1 = ['1', '100', '33']
list2 = list(map(int, list1)) #or [*map(int,list1)] unpacking도 가능

#list요소별 길이 구하기
li = [[1], [2]]
def solution(mylist):
    answer = list(map(len, mylist))
    return answer



#join의 사용, 문자열 붙이기
my_list = ['1', '100', '33']
answer = ''.join(my_list)


#2차원 리스트 1차원으로 만들기
my_list = [[1, 2], [3, 4], [5, 6]]
answer = []
for element in my_list:
    answer += element

#for문 안쓰기
my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))

# 방법 7 - numpy 라이브러리의 flatten 이용
import numpy as np
np.array(my_list).flatten().tolist()



#기본적으로 set(), dict()가 list형보다 탐색이 빠름
a = [1,2,3,4]
b = {1,2,3,4}

for i in range(10):
    if i in a:
        continue
    if i in b:
        continue

#이와 같은 형태에서 집합 자료형을 사용하는 것만 통과되는 것이 많음

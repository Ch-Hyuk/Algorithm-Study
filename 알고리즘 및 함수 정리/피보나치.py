#반복문을 이용
def solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

solution(15)

#재귀함수 이용, 시간복잡도 줄이고 제한 푸는 방식
import sys
limit_number = 150000
sys.setrecursionlimit(limit_number)

visited = {0:0,1:1}

def Fibo(n):
    if n in visited.keys():
        return visited[n]

    visited[n] = Fibo(n-1) + Fibo(n-2)
    return visited[n]

def solution(n):
    return Fibo(n) %1234567
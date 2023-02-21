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
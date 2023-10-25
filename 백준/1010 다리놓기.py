import sys
from math import factorial

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(factorial(M)//(factorial(N)*factorial(M-N)))

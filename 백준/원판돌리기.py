from collections import deque
import sys

round_dic = {}

def rec_left(radius, idx, M):
    if round_dic[radius][idx] != round_dic[radius][idx-1] or idx < -(M//2):
        round_dic[radius][idx] = 0
        return
    if round_dic[radius][idx] == round_dic[radius][idx-1]:
        rec_left(radius, idx-1)

def rec_right(radius, idx, M):
    if round_dic[radius][idx] != round_dic[radius][idx+1] or idx > M//2:
        round_dic[radius][idx] = 0
        return
    if round_dic[radius][idx] == round_dic[radius][idx+1]:
        rec_right(radius, idx+1)

def rec_radius(radius,idx, N):
    if radius > N:
        return
    if 
    if round_dic[radius][idx] == round_dic[radius+1][idx]:
        rec_radius(radius+1, idx)


N, M, T = map(int,sys.stdin.readline().split())

for radius in range(1,N+1):
    data = map(int,sys.stdin.readline().split())
    result = deque(data)
    round_dic[radius] = result


for rotation in range(T):
    x, d ,k = map(int,sys.stdin.readline().split())

    for radius in range(1,N+1):
        if radius % x == 0:
            if d == 0:
                round_dic[radius].rotate(k)
            if d == 1:
                round_dic[radius].rotate(-k)
    
    for radius in range(1,N+1):




print(round_dic)    



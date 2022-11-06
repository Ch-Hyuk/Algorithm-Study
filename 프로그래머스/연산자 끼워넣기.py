import copy
from itertools import permutations

op_list = []
res_li = []

def input_data():
    N = int(input())
    num = list(map(int,input().split()))
    op = list(map(int,input().split()))
    return N, num, op

def perm(op_list, n):
    result = []
    if n == 1:
        return op_list
    elif n > 1:
        for i in range(len(op_list)):
            ans = [j for j in op_list]
            ans.remove(op_list[i])
            for p in perm(ans, n-1):
                if op_list[i]+p not in result:
                    result.append(op_list[i]+p)
    return result

def con_op_list():
    for data in enumerate(op):
        if data[0] == 0:
            for i in range(data[1]):
                op_list.append('+')
        if data[0] == 1:
            for i in range(data[1]):
                op_list.append('-')
        if data[0] == 2:
            for i in range(data[1]):
                op_list.append('*')
        if data[0] == 3:
            for i in range(data[1]):
                op_list.append('/')

def calculation(op, a, b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        if a < 0:
            return -(-a//b)
        else:
            return a//b

if __name__ == '__main__':
    N,num,op = input_data()
    con_op_list()
    op_permu_li =list(set(permutations(op_list,N-1)))
    for data in op_permu_li:
        li1 = data
        numli = copy.deepcopy(num)
        for i in range(N):
            if i == N-1:
                res_li.append(numli[i])
            else:
                numli[i+1] = calculation(li1[i],numli[i],numli[i+1])

    print(max(res_li))
    print(min(res_li))
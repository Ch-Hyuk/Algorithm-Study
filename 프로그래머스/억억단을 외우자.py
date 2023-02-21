num={}
# def solution(e, starts):
#     divisor=[0 for i in range(e+1)]
#     for i in range(2,e+1):
#         for j in range(1,min(e//i+1,i)):
#             divisor[i*j]+=2
#     for i in range(1,int(e**(1/2))+1):
#         divisor[i**2]+=1
    
#     print(divisor)

def solution(e, starts):
    answer = []
    div_li = [0 for _ in range(e+1)]
    div_li_idx = []
    for n in range(min(starts), e+1):
        for i in range(1,min(e//n+1,n)):
            div_li[n*i] += 2
    
    for i in range(1, int(e**(1/2))+1):
        div_li[i**2] += 1
    
    max_list = []
    max = -1
    for i in div_li[::-1]:
        if max < i:
            max = i
        max_list.append(max)

    max_list = max_list[::-1]
    for i in starts:
        answer.append(div_li[i:].index(max_list[i])+i)
    return answer

def divisor(n):
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0: 
            if n in num.keys():
                num[n] +=1
                if i**2 != n:
                    num[n] +=1
            else:
                num[n] = 1
                if i**2 != n:
                    num[n] +=1


# def solution(e, starts):
#     answer = []
#     for n in range(min(starts), e+1):
#         divisor(n)

#     li = sorted(num.items(), key=lambda x: x[0],reverse=False)

#     for i in starts:
#         answer.append(sorted(li[i-1:], key=lambda x: x[1],reverse=True)[0][0])
#     return answer

e = 8
starts = [1,3,7]
print(solution(e, starts))

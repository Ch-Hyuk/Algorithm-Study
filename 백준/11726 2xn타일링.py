n= int(input())

cnt = [0 for _ in range(n+1)]

for i in range(n+1):
    if i == 0 or i == 1:
        cnt[i] = 1
    
    else:
        cnt[i] = cnt[i-1] + cnt[i-2]
    
print(cnt[-1]%10007)
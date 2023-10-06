answer = 0

N = int(input())
applicant = list(map(int,input().split()))
B, C = map(int,input().split())

for i in applicant:
    if i <= B:
        answer += 1
        continue

    if (i - B) % C:
        answer += (i - B) // C + 2
    
    else:
        answer += (i - B) // C + 1

print(answer)
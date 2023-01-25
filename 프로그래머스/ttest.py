from itertools import product

# cnt = 0
# for cwr in product([0.1,0.2,0.3,0.4], [0.1,0.2,0.3,0.4],[0.1,0.2,0.3,0.4],[0.1,0.2,0.3,0.4]):
#     print(cwr)
#     cnt += 1
# print(cnt)

a = [0.1,0.2,0.3,0.4]

# for idx,data in enumerate(a[-1::-1]):
#     print(idx, data)

cap = 2
cap_stack = [0 for i in range(cap)]
print(cap_stack)
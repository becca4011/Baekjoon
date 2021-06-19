import sys

N, C, W = map(int, sys.stdin.readline().split())
wood = list()
for i in range(N):
    wood.append(int(sys.stdin.readline()))

max_wood = max(wood)
max_res = -1
for L in range(1, max_wood + 1):
    cut_wood = list()
    cut_price = list()
    for K in range(N):
        if wood[K] >= i:
            cut_wood.append(wood[K] // L)
            if wood[K] % L == 0:
                cut_price.append((cut_wood[K] - 1) * C)
            
            elif wood[K] % L != 0:
                cut_price.append((cut_wood[K]) * C)
            
            if L * W * sum(cut_wood) < sum(cut_price):
                res = wood.count(min(wood)) * W * min(wood)
            else:
                res = (L * W * sum(cut_wood)) - sum(cut_price)

    if max_res < res:
        max_res = res

print(max_res)
# 2 * 10 * (13 + 51 + 29) - (12 + 50 + 28)
# 길이 2 / 자른 갯수는 나무 수에서 -1
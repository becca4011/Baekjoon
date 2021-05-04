import sys

T = int(sys.stdin.readline())

for i in range(T):
    clothes = dict()
    n = int(sys.stdin.readline())

    for j in range(n):
        name, type = sys.stdin.readline().split()
        clothes[type] = clothes.get(type, 1) + 1 # 옷 종류 + 1

    sum = 1
    for j in clothes.values():
        sum *= j # 옷 종류 + 1 곱하기

    print(sum - 1) # 1 빼기 (알몸인 경우)
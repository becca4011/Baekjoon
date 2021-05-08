import sys

N, M = map(int, sys.stdin.readline().split())
N_num = list(map(int, sys.stdin.readline().split()))

for k in range(1, N):
    N_num[k] = N_num[k - 1] + N_num[k] # 누적 합

for k in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i != 1:
        print(N_num[j - 1] - N_num[i - 2]) # 누적합 - 앞의 누적합(구간 포함 X 부분)
    else:
        print(N_num[j - 1]) # i가 1이면 구한 누적합 그대로
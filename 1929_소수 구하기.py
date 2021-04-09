import sys

M, N = map(int, sys.stdin.readline().split())

# 에라토스테네스의 체
prime_num = [False, False] + [True] * (N - 1)
primes = []

for i in range(2, N + 1):
    if prime_num[i]:
        primes.append(i)
        for j in range(2 * i, N + 1, i): # 초기값, 마지막값, 증가값
            prime_num[j] = False

for i in primes:
    if i >= M:
        print(i)
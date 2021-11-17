# import sys


# def prime(n):
#     if n == 1:
#         return False
#     else:
#         for i in range(2, n):
#             for j in range(i * i, n, i):
#                 if n % j == 0:
#                     return False
#         return True


# N = int(sys.stdin.readline())

# if prime:
#     print()
# else:
#     print(N - 1)

import sys

N = int(sys.stdin.readline())

cnt = 0
for i in range(N - 1, 1, -1):
    cnt += 1
    if N % i == 0:
        break

print(cnt)
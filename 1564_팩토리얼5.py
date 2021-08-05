import sys
import math

N = int(sys.stdin.readline())

fac = 1
for i in range(1, N + 1):
    fac *= i
    while fac % 10 == 0:
        fac //= 10
    fac %= 100000000  # 나눠주지 않으면 시간 초과

fac %= 100000  # 5자리 맞추기
print(str(fac).zfill(5))

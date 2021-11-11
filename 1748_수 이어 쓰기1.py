import sys

# 1자리 9 = 9 * 10^0
# 2자리 90 = 9 * 10^1
# 3자리 900 = 9 * 10^2

# 15 : 9 + (15 - 10 + 1) * 2 = 21
# 120 : 9 + 90 * 2 + (120 - 100 + 1) * 3 = 252

N = int(sys.stdin.readline())

if N < 10:
    print(N)
else:
    sum = 0
    for i in range(len(str(N)) - 1):
        sum += 9 * (10 ** i) * (i + 1)

    print(sum + (N - 10 ** (len(str(N)) - 1) + 1) * len(str(N)))

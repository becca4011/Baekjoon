import sys

N = int(sys.stdin.readline())

if N < 10:
    print(N % 1234567)
else:
    sum = 0
    for i in range(len(str(N)) - 1):
        sum += 9 * (10 ** i) * (i + 1)
    sum += len(str(N)) * (N - (10 ** (len(str(N)) - 1)) + 1)
    print(sum % 1234567)

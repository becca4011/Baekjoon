import sys

n = int(sys.stdin.readline())
li = [1, 3] + [0] * (n - 2)

for i in range(2, n):
    li[i] = li[i - 2] * 2 + li[i - 1]

print(li[n - 1] % 10007)
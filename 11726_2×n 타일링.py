import sys

n = int(sys.stdin.readline())
li = [1, 2, 3] + [0] * (n - 3)

for i in range(3, n):
    li[i] = li[i - 2] + li[i - 1]

print(li[n - 1] % 10007)
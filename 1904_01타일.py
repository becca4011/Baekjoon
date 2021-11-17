import sys

li = [1, 2]
for i in range(2, 1000000):
    li.append((li[i - 2] + li[i - 1]) % 15746)

N = int(sys.stdin.readline())
print(li[N - 1])

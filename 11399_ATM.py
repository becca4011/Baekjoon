import sys

N = int(sys.stdin.readline())
P = sorted(list(map(int, sys.stdin.readline().split())))

add = 0
for i in range(1, len(P) + 1):
    add += sum(P[0:i])

print(add)
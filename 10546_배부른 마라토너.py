import sys

N = int(sys.stdin.readline())

dt = dict()
for i in range(N + N - 1):
    p = sys.stdin.readline().rstrip()
    dt[p] = dt.get(p, 0) + 1

for k, v in dt.items():
    if v % 2 != 0:
        print(k)
        break

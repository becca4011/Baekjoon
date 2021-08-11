import sys

N = int(sys.stdin.readline())
dt = dict()
for i in range(N):
    S = "".join(sorted(list(sys.stdin.readline().rstrip())))
    dt[S] = dt.get(S, 0) + 1

print(len(dt))

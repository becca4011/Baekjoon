import sys

N, M = map(int, sys.stdin.readline().split())

dt = dict()
for i in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        dt[word] = dt.get(word, 0) + 1

dt = sorted(dt.items(), key=(lambda x: (-x[1], -len(x[0]), x[0])))
for i in dt:
    print(i[0])

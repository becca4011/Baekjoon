import sys

N = int(sys.stdin.readline())
dt = dict()
for i in range(N):
    file = sys.stdin.readline().rstrip().split(".")[1]
    dt[file] = dt.get(file, 0) + 1

dt = sorted(dt.items(), key=(lambda x: x[0]))
for key, value in dt:
    print(key, value)

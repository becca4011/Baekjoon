import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

X_dict = {i : X[i] for i in range(len(X))}
X_sort = sorted(X_dict.items(), key=(lambda x : x[1]))
X_dict = dict((y, x) for x, y in X_sort)

m = 0
for key in X_dict.keys():
    X_dict[key] = m
    m += 1

for i in X:
    print(X_dict[i], end = ' ')
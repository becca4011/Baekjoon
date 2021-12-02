import sys

while True:
    dt = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    A, B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0:
        break

    for i in range(A, B + 1):
        save = map(int, str(i))
        for j in save:
            dt[int(j)] += 1

    for v in dt.values():
        print(v, end=" ")
    print()

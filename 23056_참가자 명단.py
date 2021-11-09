import sys

N, M = map(int, sys.stdin.readline().split())
li = list()
dt = dict()

while True:
    join = sys.stdin.readline().rstrip()

    if join == "0 0":
        break

    join = join.split()
    dt[join[0]] = dt.get(join[0], 0) + 1

    if dt[join[0]] <= M:
        li.append(join)

li = sorted(li, key=lambda x: (int(x[0]), len(x[1]), x[1]))
blue = list()
white = list()

for i in range(len(li)):
    if int(li[i][0]) % 2 == 0:
        white.append(" ".join(li[i]))
    else:
        blue.append(" ".join(li[i]))

for i in blue:
    print(i)
for i in white:
    print(i)

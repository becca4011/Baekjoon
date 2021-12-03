import sys

R, C = map(int, sys.stdin.readline().split())

li = list()
for i in range(R):
    li.append(sys.stdin.readline().rstrip())
li_rev = list(map(list, zip(*li)))

res = list()
for i in li:
    save = i.split("#")
    for j in save:
        if len(j) > 1:
            res.append(j)

for i in li_rev:
    save = "".join(i).split("#")
    for j in save:
        if len(j) > 1:
            res.append(j)

res.sort()
print(res[0])

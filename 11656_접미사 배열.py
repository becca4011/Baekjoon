import sys

S = sys.stdin.readline().rstrip()
li = list()

for i in range(len(S)):
    li.append(S[i:])

li.sort()
for i in li:
    print(i)

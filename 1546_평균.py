import sys

n = int(sys.stdin.readline())
score = sys.stdin.readline().split()
iscore = list(map(int, score))

li = []
for i in iscore:
    li.append(i / max(iscore) * 100)

print(sum(li, 0.0) / n)

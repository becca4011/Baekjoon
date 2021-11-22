import sys
from itertools import combinations

N = int(sys.stdin.readline())
war = sys.stdin.readline().split()
answer = sys.stdin.readline().split()

war = {w: i for i, w in enumerate(war)}
answer = list(combinations(answer, 2))

cnt = 0
for i in range(len(answer)):
    if war[answer[i][0]] < war[answer[i][1]]:
        cnt += 1

print(str(cnt) + "/" + str(N * (N - 1) // 2))

import sys

cnt = sys.stdin.readline().rstrip()
quiz = []
res = 0
s = 0

for i in range(int(cnt)):
    quiz.append(sys.stdin.readline().rstrip())

for i in range(int(cnt)):
    for j in range(len(quiz[i])):
        if quiz[i][j] == 'O':
            s += 1
        elif quiz[i][j] == 'X':
            s = 0
        res += s
    print(res)
    s = 0
    res = 0

import sys

di = {0: "{}", 1: "{{}}", 2: "{{},{{}}}"}
for i in range(3, 16):
    di[i] = "{"
    for j in range(i):
        if j != i - 1:
            di[i] += di[j] + ","
        else:
            di[i] += di[j]
    di[i] += "}"
di_rev = dict((v, k) for k, v in di.items())

T = int(sys.stdin.readline())

for i in range(T):
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()
    cnt = di_rev[a] + di_rev[b]
    print(di[cnt])

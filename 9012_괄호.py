import sys

num = sys.stdin.readline().rstrip()
ps = []

for n in range(int(num)):
    ps.append(sys.stdin.readline().rstrip())

cnt = 0
for i in range(int(num)):
    for p in ps[i]:
        if cnt < 0:
            break
        if p == '(':
            cnt += 1
        elif p == ')':
            cnt -= 1

    if cnt == 0:
        print("YES")
    else:
        print("NO")
    cnt = 0
